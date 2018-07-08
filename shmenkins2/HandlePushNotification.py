import json
import logging
import os

import boto3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

artifact_updated_queue = boto3.resource('sqs').Queue(os.environ["ARTIFACT_UPDATED_QUEUE_URL"])


def run(event, context):
    logger.info(f"start")

    body = json.loads(event["body"])
    url = body["repository"]["url"]

    artifact_updated_queue.send_message(MessageBody=json.dumps({"url": url}))

    logger.info(f"finish")
    return {"statusCode": 201, "body": ""}
