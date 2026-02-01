from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="investing-bbs",
    version="1.1.0",
    author="linproxy",
    author_email="",
    description="A BBS-style CLI for viewing financial markets data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hsuanchenlin/investing_cli",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial",
        "Topic :: Terminals",
    ],
    python_requires=">=3.7",
    install_requires=[
        "rich>=13.0.0",
        "requests>=2.28.0",
        "python-dateutil>=2.8.0",
        # readchar removed - using native termios instead
    ],
    entry_points={
        "console_scripts": [
            "investing-bbs=investing_bbs.main:main",
        ],
    },
)
