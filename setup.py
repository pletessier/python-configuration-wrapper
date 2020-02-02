from setuptools import setup

setup(
    name='python-configuration-wrapper',
    version='1.0.2',
    description='A wrapper of python-configuration',
    url="https://github.com/pletessier/python-configuration-wrapper",
    author='Pierre Letessier',
    keywords=["configuration"],
    packages=['python_configuration_wrapper'],
    install_requires=['python-configuration[toml,yaml]~=0.6', 'singleton~=0.1', 'dotmap~=1.3'],
)
