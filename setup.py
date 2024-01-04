from setuptools import find_packages, setup
from requirements import parse

def get_requirements(file_path: str) -> list:
    '''This function returns the list of packages to be installed'''
    with open(file_path) as f:
        req = parse(f)
        return [str(package.req) for package in req]

setup(
    name="Ames House price prediction",
    version="0.0.1",
    author="Himanshu Choudhary",
    author_email="Hchoudhary525@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


