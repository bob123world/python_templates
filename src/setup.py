from setuptools import find_packages, setup

with open("config/requirements.txt") as requirement_file:
    requirements = requirement_file.read().split()

setup(
    name="simple_package",
    description="A simple package.",
    version="1.0.0",
    author="Name",
    author_email="Name@domain.com",
    install_requires=requirements,
    packages=find_packages(
        exclude=["project1", "project2"]
    ),  # package = any folder with an __init__.py file
)
