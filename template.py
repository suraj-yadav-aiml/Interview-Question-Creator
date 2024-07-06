import os
from pathlib import Path
import logging
from typing import List

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


class TemplateCreator:
    """
    A class responsible for creating files and their parent directories.
    """

    def __init__(self, filepaths: List[str]):
        """
        Initializes the TemplateCreator with a list of file paths.

        Args:
            filepaths: A list of file paths to create.
        """
        self.filepaths = filepaths

    def create_files(self) -> None:
        """
        Creates empty files and their parent directories if they don't exist.
        """
        for filepath in self.filepaths:
            filepath = Path(filepath)  

            # Split the path into directory and filename components
            filedir, filename = os.path.split(filepath)

            if filedir != "":  # Check if there are parent directories to create
                os.makedirs(filedir, exist_ok=True)  
                logging.info(f"Creating directory {filedir} for the files {filename}")

            # Check if the file doesn't exist or is empty (0 bytes)
            if not filepath.is_file() or filepath.stat().st_size == 0: 
                filepath.touch()  # Create an empty file
                logging.info(f"Creating empty file : {filepath}")
            else:
                logging.info(f"{filename} is already exists")

if __name__ == "__main__":

    list_of_files = [
        "src/__init__.py",
        "src/helper.py",
        "src/prompt.py",
        ".env",
        "requirements.txt",
        "setup.py",
        "research/trials.ipynb",
        "app.py",
    ]

    creator = TemplateCreator(list_of_files)
    creator.create_files()
