import json
import logging
import os

import boto3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

build_scheduled_topic = boto3.resource('sns').Topic(os.environ["BUILD_SCHEDULED_TOPIC_ARN"])


def run(event, context):
    sns_record = event["Records"][0]["Sns"]
    message = json.loads(sns_record["Message"])
    url = message["url"]
    build_scheduled_topic.publish(Message=json.dumps({"url": url}))
