from setuptools import setup

setup(
    name = "test_package",
    version = "1.0",
    description = "Test package with greet",
    author = "Daniel",
    author_email = "jdanielcarranzal@hotmail.com",
    url = "x",
    packages = ['test_package']
)
# Use the command to export: python3 setup.py sdist
# Use the command to install: pip3 install test_package-1.0.tar.gz 