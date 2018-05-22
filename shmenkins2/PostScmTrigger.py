import os
import logging
import boto3
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    logger.info(f"start")

    body = json.loads(event["body"])
    logger.info(f"body={body}")

    logger.info(f"finish")
    return {"statusCode": 201, "body": json.dumps(body)}
