import json
import logging
import os

import boto3
import records

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

db = records.Database(os.environ["DB_URL"])
artifact_updated_queue = boto3.resource("sqs").Queue(os.environ["ARTIFACT_UPDATED_QUEUE_URL"])


def run(event, context):
    logger.info(f"start")

    body = json.loads(event["body"])
    url = body["repository"]["url"]

    logger.info(f"url={url}")
    try:
        rows = db.query("select id from scm_trigger where url=:url", url=url)
        logger.info(f"found {len(rows.all())} src artifacts")
    except Exception as e:
        logger.error(e)
        return {"statusCode": 500, "body": "Internal server error"}

    if len(rows) > 0:
        messages = [create_message(row["id"], url) for row in rows]
        # SQS limit is 10 messages in a batch
        max_batch_size = 10
        message_batches = [messages[i:i + max_batch_size] for i in range(0, len(messages), max_batch_size)]
        for batch in message_batches:
            artifact_updated_queue.send_messages(Entries=batch)

    logger.info(f"finish")
    return {"statusCode": 201, "body": ""}


def create_message(artifact_id, url):
    return {
        "Id": str(artifact_id),
        "MessageBody": json.dumps({"id": artifact_id, "url": url})
    }
