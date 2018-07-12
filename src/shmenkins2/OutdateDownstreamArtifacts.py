import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    logger.info(f"start; event={event}")

    for message in event["Records"]:
        artifact = json.loads(message["body"])
        outdate_downstream_artifacts(artifact["id"])


def outdate_downstream_artifacts(artifact_id):
    logger.info(f"outdated downstream artifact for; artifact_id={artifact_id}")


# sqs message example
#{
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
#}
