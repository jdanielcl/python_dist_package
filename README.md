# Instructions

## Create a module

Create a module for example, test_package and create inside the file __init__.py

## Create installer

Create a file setup.py writing the basic information about the package

```python
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
```

## Export

Export the package using the following command

```shell
python3 setup.py sdist
```

## Import

Once you export the package the system will create a "dist" directory, use the file with extension .gz to install the package using the following comand

```shell
pip3 install test_package-1.0.tar.gz 
```