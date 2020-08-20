from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python-configuration-wrapper',
    version='1.1.0',
    description='A wrapper of python-configuration',
    url="https://github.com/pletessier/python-configuration-wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Pierre Letessier',
    keywords=["configuration"],
    packages=['python_configuration_wrapper'],
    install_requires=['python-configuration[toml,yaml]~=0.6', 'singleton~=0.1', 'dotmap~=1.3'],
)
