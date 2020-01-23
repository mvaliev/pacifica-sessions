#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Global configuration options expressed in environment variables."""
from configparser import ConfigParser
from os import getenv
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
PROJ_DIR = THIS_DIR.parent
PROJ_DIR_PARENT = PROJ_DIR.parent

CP_CONFIG_FILE_DEFAULT = str(PROJ_DIR.joinpath('server.conf'))
DB_FILE_DEFAULT = str(PROJ_DIR.joinpath('session.db'))
CP_CONFIG_FILE = getenv('SESSION_CP_CONFIG_FILE', CP_CONFIG_FILE_DEFAULT)

GLOBAL_CONFIG_DEFAULT = str(PROJ_DIR_PARENT.joinpath('.session.conf'))
GLOBAL_CONFIG = getenv('DATABASE_CONFIG_FILE', GLOBAL_CONFIG_DEFAULT)

_PROJECT_ENV = {'home_user':getenv('HOME'),
                'home_project':PROJ_DIR_PARENT}


config = ConfigParser(_PROJECT_ENV)
config.read(GLOBAL_CONFIG)


