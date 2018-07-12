import json
import logging
import os

import boto3
import records

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

db = records.Database(os.environ["DB_URL"])
artifact_outdated_queue = boto3.resource("sqs").Queue(os.environ["ARTIFACT_OUTDATED_QUEUE_URL"])


def run(event, context):
    logger.info(f"start; event={event}")

    for message in event["Records"]:
        scm_repo = json.loads(message["body"])
        outdate_downstream_artifacts_for_scm_repo(scm_repo["id"])


def outdate_downstream_artifacts_for_scm_repo(scm_repo_id):
    rows = db.query(
        "select artifact_group_id"
        "    from scm_repo__artifact_group"
        "    where scm_repo_id=:scm_repo_id", scm_repo_id=scm_repo_id)
    row_count = len(rows.all())  # without .all() none of the rows are fetched
    logger.info(f"found downstream artifact;"
                f" scm_repo_id={scm_repo_id}, row_count={row_count}")

    if row_count > 0:
        messages = [create_message(row["artifact_group_id"]) for row in rows]
        # SQS limit is 10 messages in a batch
        max_batch_size = 10
        message_batches = [messages[i:i + max_batch_size] for i in range(0, len(messages), max_batch_size)]
        for batch in message_batches:
            artifact_outdated_queue.send_messages(Entries=batch)


def create_message(artifact_id):
    return {
        "Id": str(artifact_id),
        "MessageBody": json.dumps({"id": artifact_id})
    }

# sqs message example
# {
#    "Records": [
#        {
#            "messageId": "50ece427-4c82-4799-8103-cb16938893e6",
#            "receiptHandle": "xxx",
#            "body": "{\"url\": \"https://github.com/bob/demo-simple-web\"}",
#            "attributes": {
#                "ApproximateReceiveCount": "1",
#                "SentTimestamp": "1531013273409",
#                "SenderId": "AROAJ6W63ZSHUUUUZH5KE:shmenkins2-dev-HandlePushNotification",
#                "ApproximateFirstReceiveTimestamp": "1531013273442"
#            },
#            "messageAttributes": {},
#            "md5OfBody": "e05e5de66e1180ca3935fc7b7e811112",
#            "eventSource": "aws:sqs",
#            "eventSourceARN": "arn:aws:sqs:us-west-2:000000000000:shmenkins2-dev-artifact_updated_queue",
#            "awsRegion": "us-west-2"
#        }
#    ]
# }
