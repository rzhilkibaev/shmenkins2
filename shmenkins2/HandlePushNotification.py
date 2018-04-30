import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    logger.info(f"start")
    logger.info(f"finish")
    return {"statusCode": 201, "body": ""}
