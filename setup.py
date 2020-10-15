from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="azcam-mag",
    version="20.1",
    description="azcam extension for OCIW ITL Magellan CCD controllers",
    long_description=long_description,
    author="Michael Lesser",
    author_email="mlesser@arizona.edu",
    keywords="python parameters",
    packages=find_packages(),
    zip_safe=False,
    install_requires=["azcam"],
)
