import json
import logging
import os

import records
from sqlalchemy import text

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

shmenkins_db_url = os.environ["DB_URL"]

db = records.Database(shmenkins_db_url)


def run(event, context):
    logger.info(f"start; event={event}")

    try:
        body = json.loads(event["body"])
        url = body["url"]
    except Exception as e:
        logger.error(e)
        return {"statusCode": 400, "body": "Bad Request"}

    try:
        with db.transaction():
            cursor = db.db.execute(text("insert into scm_trigger(url) values(:url)"), url=url)
            body["id"] = cursor.lastrowid
        response_body = json.dumps(body)
    except Exception as e:
        logger.error(e)
        return {"statusCode": 500, "body": "Internal server error"}

    logger.info(f"finish")
    return {"statusCode": 201, "body": response_body}
