import configparser
import json
import os

cfg = configparser.ConfigParser()
cfg.read("config.ini")

os.environ["DB_URL"] = str(cfg["default"]["shmenkins_db_url"])
os.environ["ARTIFACT_UPDATED_QUEUE_URL"] = str(cfg["default"]["artifact_updated_queue_url"])

from shmenkins2 import HandlePushNotification
from shmenkins2 import PostScmTrigger


def test_post_scm_trigger():
    event = {"body": json.dumps({"url": "abc"})}
    ctx = None
    response = PostScmTrigger.run(event, ctx)

    assert response["statusCode"] == 201

    body = json.loads(response["body"])

    assert body["url"] == "abc"
    assert body["id"] > 0


def test_handle_push_notification():
    event = {"body": json.dumps({"repository": {"url": "abc"}})}
    ctx = None
    response = HandlePushNotification.run(event, ctx)

    assert response["statusCode"] == 201
