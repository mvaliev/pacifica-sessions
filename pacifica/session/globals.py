#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Global configuration options expressed in environment variables."""
from os import getenv
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
PROJ_DIR = THIS_DIR.parent

CP_CONFIG_FILE_DEFAULT = str(PROJ_DIR.joinpath('server.conf'))
CP_CONFIG_FILE = getenv('SESSION_CP_CONFIG_FILE', CP_CONFIG_FILE_DEFAULT)


if __name__ == '__main__':
    print(type(CP_CONFIG_FILE), CP_CONFIG_FILE)
