import os
import logging
import boto3
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

build_requested_topic = boto3.resource('sns').Topic(os.environ["BUILD_REQUESTED_TOPIC_ARN"])


def run(event, context):
    logger.info(f"start")

    body = json.loads(event["body"])
    url = body["repository"]["url"]

    build_requested_topic.publish(Message=json.dumps({"url": url}))

    logger.info(f"finish")
    return {"statusCode": 201, "body": ""}
