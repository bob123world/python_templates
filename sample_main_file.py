import logging
import os
import time
import traceback

from dotenv import load_dotenv
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import Progress

console = Console()


def main():
    """Sample main function"""
    console.print("[green]program started...")
    logger.info("Test row added for start")
    with Progress() as progress:

        task1 = progress.add_task("[red]Downloading...", total=1000)

        while not progress.finished:
            progress.update(task1, advance=0.5)
            time.sleep(0.02)
    console.print("[green]program ended...")
    logger.info("Test row added for end")
    logger.error("program ended!")


if __name__ == "__main__":
    load_dotenv()

    # create logger
    logger = logging.getLogger("sample_main")
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(os.environ.get("LOGFILE"))
    fh.setLevel(logging.DEBUG)
    # create Rich handler with a higher log level
    rh = RichHandler()
    rh.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    rh.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(rh)

    main()
