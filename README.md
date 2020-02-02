# Python Configuration Wrapper

This lib is basically a wrapper of the [python-configuration](https://pypi.org/project/python-configuration/).

It aims at making configuration easy !

## Features

Read multi-level configuration values from multiple sources (precedency ordered):
1. Command line arguments given by `--additional-config` or `-C` parameter.

    Example: 
    ```
    python app.py -C "database.dialect=postgresql" --additional-config "database.host=postgres.mydomain.org" -C "database.user=admin"
    ```
1. Environment variables starting with prefix set in the `CONFIG_PREFIX` environment variable. Level separator is `__` (double underscore).

   Example:
   ```
   CONFIG_PREFIX=TEST TEST__database__user=root python app.py
   ```
   
1. Config directories given by `--config-path` or `-P` parameter. The value of this parameter must be a directory path in which the sub-directories are multi-level keys, and plain-text files content are values. It's very practical when using secrets in containers.  

   Example:
   ```.bash
   mkdir /var/run/secrets/database -p
   echo -n 123456 > /var/run/secrets/database/password
   python app.py --config-path /var/run/secrets
   ```
   
1. Config files given by `--config-file` or `-F` parameter. File formats must be among those handled by [python-configuration](https://pypi.org/project/python-configuration/):
    * json
    * ini
    * yaml
    * toml
    * python
    
    Example:
    ```.bash
    python app.py -F config.json --config-file config.yaml
    ```

## Installation
```
pip install python-configuration-wrapper
```

## Usage
```
# import the config object from the module
# you can do this in every python file you want
from python_configuration_wrapper import config

# get some value from a multi-level key
myvalue = config.myfirstlevel.mysecondlevel.mykey
```

## Example 

See [test](./test)