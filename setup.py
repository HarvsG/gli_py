from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="gli_py",
    version="0.0.1",
    author="HarvsG",
    author_email="doctor@codingdoctor.co.uk",
    description="A Python 3 API wrapper for the API on GL-inet routers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HarvsG/gli_py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License, version 3",
        "Operating System :: OS Independent",
    ]
)