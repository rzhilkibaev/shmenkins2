import os

import records
import requests
import configparser
import json

cfg = configparser.ConfigParser()
cfg.read("config.ini")

os.environ["DB_URL"] = str(cfg["default"]["shmenkins_db_url"])

from shmenkins2 import PostScmTrigger


def test_post_scm_trigger():
    event = {"body": json.dumps({"url": "abc"})}
    ctx = None
    response = PostScmTrigger.run(event, ctx)
    print(str(response))

    assert response["statusCode"] == 201

    body = json.loads(response["body"])

    assert body["url"] == "abc"
    assert body["id"] > 0
