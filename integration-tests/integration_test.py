import configparser
import json
import os

cfg = configparser.ConfigParser()

this_file_dir = os.path.dirname(os.path.abspath(__file__))
cfg.read(f"{this_file_dir}/config.ini")

os.environ["DB_URL"] = str(cfg["default"]["shmenkins_db_url"])
os.environ["ARTIFACT_UPDATED_QUEUE_URL"] = str(cfg["default"]["artifact_updated_queue_url"])
os.environ["ARTIFACT_OUTDATED_QUEUE_URL"] = str(cfg["default"]["artifact_outdated_queue_url"])

from shmenkins2 import HandlePushNotification
from shmenkins2 import PostScmRepo
from shmenkins2 import OutdateDownstreamArtifactsForScmRepo


def test_outdate_downstream_aftifacts_for_scm_repo():
    event = {"Records": [
        {"body": json.dumps({"id": "4"})}
    ]}
    ctx = None
    # just run to see if it finishes without failing
    OutdateDownstreamArtifactsForScmRepo.run(event, ctx)


def test_post_scm_repo():
    event = {"body": json.dumps({"url": "abc"})}
    ctx = None
    response = PostScmRepo.run(event, ctx)

    assert response["statusCode"] == 201

    body = json.loads(response["body"])

    assert body["url"] == "abc"
    assert body["id"] > 0


def test_handle_push_notification():
    event = {"body": json.dumps({"repository": {"url": "abc"}})}
    ctx = None
    response = HandlePushNotification.run(event, ctx)

    assert response["statusCode"] == 201
