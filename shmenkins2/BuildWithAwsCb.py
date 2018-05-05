import hashlib
import json
import logging
import os

import boto3
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

cb = boto3.client("codebuild")
cb_service_role_arn = os.environ["CB_SERVICE_ROLE_ARN"]


def run(event, context):
    sns_record = event["Records"][0]["Sns"]
    message = json.loads(sns_record["Message"])
    url = message["url"]
    put_project(url)


def put_project(url):
    project_name = hashlib.sha256(url.encode()).hexdigest()
    try:
        # update the cb project without checking if it exists first
        # most of the time the project is already there
        cb_update_project(project_name, url)
    except ClientError as e:
        if is_resource_not_found_error(e):
            cb_create_project(project_name, url)
        else:
            raise e

    return project_name


def cb_create_project(project_name: str, url: str) -> None:
    logger.debug(f"Creating AWS CodeBuild project; project_name={project_name}, url={url}")
    project = cb.create_project(
        name=project_name,
        description=url,
        source={"type": "GITHUB", "location": url},
        artifacts={"type": "NO_ARTIFACTS"},
        environment={"type": "LINUX_CONTAINER", "image": "rzhilkibaev/jst", "computeType": "BUILD_GENERAL1_SMALL"},
        serviceRole=cb_service_role_arn
    )
    logger.debug(f"Created AWS CodeBuild project; project_name={project_name}, url={url}, project={project}")


def cb_update_project(project_name: str, url: str) -> None:
    logger.debug(f"Updating AWS CodeBuild project; project_name={project_name}, url={url}")
    project = cb.update_project(
        name=project_name,
        description=url,
        source={"type": "GITHUB", "location": url},
        artifacts={"type": "NO_ARTIFACTS"},
        environment={"type": "LINUX_CONTAINER", "image": "rzhilkibaev/jst", "computeType": "BUILD_GENERAL1_SMALL"},
        serviceRole=cb_service_role_arn
    )
    logger.debug(f"Updated AWS CodeBuild project; project_name={project_name}, url={url}, project={project}")


def is_resource_not_found_error(e: ClientError) -> bool:
    try:
        return e.response["Error"]["Code"] == "ResourceNotFoundException"
    except:
        return False
