from os import getcwd, path
from setuptools import find_packages, setup

def get_requirements(filepath: str):
    return [l.strip() for l in open(path.join(getcwd(),filepath),"r",encoding="utf-16")]

setup(
    name="tai",
    version="0.0.2",
    author="ramyres110",
    description="Aplicação de terminal que utiliza o poder das LLMs",
    url="https://github.com/ramyres110/terminai-cli",
    platforms=["win32"],
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)