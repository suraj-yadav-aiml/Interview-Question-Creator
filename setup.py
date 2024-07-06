from setuptools import setup, find_packages  
from typing import List
import os

PackageList = List[str]

def get_requirements(filepath: str = "requirements.txt") -> PackageList:
    """
    Reads package requirements from a file.

    Args:
        filepath: Path to the requirements file (default: "requirements.txt").

    Returns:
        A list of package names.
    """
    with open(filepath) as file_obj:
        requirements = [line.strip() for line in file_obj][:-1] # except -e .
    return requirements


setup(
    name="Interview Question Creator",
    version='0.0.1',  
    author="Suraj Yadav",
    author_email="suraj.yadav.aiml@gmail.com",
    description="Interview Question Creator",  
    long_description=open("README.md").read() if os.path.exists("README.md") else "", 
    url="https://github.com/suraj-yadav-aiml/Interview-Question-Creator",  
    packages=find_packages(),
    install_requires=get_requirements(),  
    python_requires='>=3.10',  
)
