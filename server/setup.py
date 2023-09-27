from pathlib import Path

from setuptools import setup

from supernice import __version__


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(Path(__file__).parent / "docs" / "README.md").read()


def read_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()


settings = dict(
    name="supernice",
    packages=["supernice"],
    version=__version__,
    author="Conrad Lippert-Zajaczkowski",
    author_email="conrad@swapnice.com",
    description=("Python starter project"),
    license="MIT",
    keywords="python",
    url="https://supernice.ai/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    python_requires=">=3.11",
    install_requires=read_requirements("requirements.txt"),
    tests_require=read_requirements("dev-requirements.txt"),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)


if __name__ == "__main__":
    setup(**settings)
