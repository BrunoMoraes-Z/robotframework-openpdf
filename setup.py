import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="['openpdflibrary']",
    version="0.1.0",
    author="Bruno Moraes",
    author_email="moraes.7bruno@gmail.com",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BrunoMoraes-Z/robotframework-openpdf",
    packages=["OpenPDFLibrary"],
    install_requires=['robotframework', 'tika'],
    zip_safe=False
)