#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Global configuration options expressed in environment variables."""
from os import getenv
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
PROJ_DIR = THIS_DIR.parent.parent

CP_CONFIG_FILE_DEFAULT = str(PROJ_DIR.joinpath('server.conf'))
CP_CONFIG_FILE = getenv('SESSION_CP_CONFIG_FILE', CP_CONFIG_FILE_DEFAULT)

print(type(CP_CONFIG_FILE))
# CONFIG_FILE = getenv('INGEST_CONFIG', join(
#     expanduser('~'), '.pacifica-ingest', 'config.ini'))
