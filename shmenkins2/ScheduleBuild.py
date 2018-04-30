import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    logger.info(f"start; event={json.dumps(event)}")
    logger.info(f"Scheduling build")
    logger.info(f"finish")
