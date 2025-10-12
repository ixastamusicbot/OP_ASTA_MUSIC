import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import config
from ..logging import LOGGER

logger = LOGGER(__name__)


async def install_req(cmd: str) -> Tuple[str, str, int, int]:
    """Asynchronous requirements installer"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def git_async():
    """Async git setup to avoid blocking startup"""
    REPO_LINK = config.UPSTREAM_REPO
    UPSTREAM_REPO = REPO_LINK
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"

    try:
        repo = Repo()
        logger.info(f"Git Client Found [VPS DEPLOYER]")
    except (GitCommandError, InvalidGitRepositoryError):
        try:
            repo = Repo.init()
        except Exception:
            logger.info("Failed to init git repo")
            return

    # Setup origin remote
    try:
        if "origin" not in repo.remotes:
            repo.create_remote("origin", UPSTREAM_REPO)
        origin = repo.remote("origin")
    except Exception:
        origin = repo.remote("origin")

    try:
        origin.fetch(config.UPSTREAM_BRANCH)
        origin.pull(config.UPSTREAM_BRANCH)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    except Exception as e:
        logger.info(f"Git fetch/pull skipped: {e}")

    # Install requirements async (non-blocking)
    try:
        await install_req("pip3 install --no-cache-dir -r requirements.txt")
        logger.info(f"Fetched updates and installed requirements successfully")
    except Exception as e:
        logger.info(f"Requirement installation failed: {e}")


def git():
    """Wrapper to run async git safely"""
    try:
        asyncio.get_event_loop().run_until_complete(git_async())
    except RuntimeError:
        # In case event loop is already running (e.g., in some environments)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(git_async())
