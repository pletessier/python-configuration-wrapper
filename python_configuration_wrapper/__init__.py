# Copyright (C) 2019 Pierre Letessier
# This source code is licensed under the BSD 3 license found in the
# LICENSE file in the root directory of this source tree.

import argparse
import ast
import os
import sys

from config import config as python_config
from dotmap import DotMap
from singleton.singleton import Singleton


def infer_best_type(v):
    try:
        return ast.literal_eval(v)
    except (ValueError, SyntaxError):
        return v


@Singleton
class Configuration:
    def __init__(self):
        app_name = os.getenv('CONFIG_APP_NAME', "APP")
        prefix = os.getenv('CONFIG_PREFIX', "APP")

        parser = argparse.ArgumentParser(prog=app_name)
        parser.add_argument('--config-file', '-F', dest='config_files', action='append', type=str,
                            help='a list of yaml config files')
        parser.add_argument('--config-path', '-P', dest='config_paths', action='append', type=str,
                            help='a list of directories in which the file paths are keys and file contents are value')
        parser.add_argument('--additional-config', '-C', dest='additional_config', action='append', type=str,
                            help='a list of dotted.key=value configs')
        args, unknowns = parser.parse_known_args()

        if unknowns:
            parser.print_usage()
            sys.exit(1)

        configurations = list()

        if args.additional_config:
            kv_args = dict(i.split("=", maxsplit=1) for i in args.additional_config)
            for k, v in kv_args.items():
                kv_args[k] = infer_best_type(v)

            configurations.append(kv_args)

        configurations.append("env")
        if args.config_paths:
            configurations.extend(args.config_paths)
        if args.config_files:
            configurations.extend(args.config_files)
        else:
            if os.path.isfile('config.yaml'):
                configurations.append('config.yaml')
            elif os.path.isfile('config.json'):
                configurations.append('config.json')
            elif os.path.isfile('config.ini'):
                configurations.append('config.ini')
            elif os.path.isfile('config.toml'):
                configurations.append('config.toml')
            elif os.path.isfile('config.python'):
                configurations.append('config.python')

        conf_set = python_config(*configurations, prefix=prefix, remove_level=0)

        tempdict = dict()

        for key, value in conf_set.as_dict().items():
            tree = key.split('.')
            root = tempdict
            for i, b in enumerate(tree):
                if b not in root:
                    if (i + 1) == len(tree):
                        root[b] = value
                    else:
                        root[b] = dict()
                root = root[b]
        self.dict = DotMap(tempdict, _dynamic=False)


config = Configuration.instance().dict
