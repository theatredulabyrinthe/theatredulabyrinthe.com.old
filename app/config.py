import os


class Config:
    SECRET_KEY = "1fd6f521af7eb7919a8a816e52a30449"


"""
import os
import json

with open("/etc/config.json") as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get("SECRET_KEY")
"""

