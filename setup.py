from setuptools import find_packages, setup
from setuptools.command.install import install
from setuptools import setup, find_packages
from pip._internal.req import parse_requirements

# Function to parse requirements.txt file
def parse_requirements_file():
    reqs = parse_requirements('requirements.txt', session=False)
    return [str(ir.requirement) for ir in reqs]

setup(
    name="Ames House price prediction",
    version="0.0.1",
    author="Himanshu Choudhary",
    author_email="Hchoudhary525@gmail.com",
    packages=find_packages(),
    install_requires=parse_requirements_file()
)



