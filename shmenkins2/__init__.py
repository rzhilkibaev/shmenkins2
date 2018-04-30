import os
import configparser

# load deployment specific env variables from config.ini if it exists
cfg = configparser.ConfigParser()
cfg.read("config.ini")
if cfg.has_section("default"):
    for (k, v) in cfg.items("default"):
        os.environ[k] = v
