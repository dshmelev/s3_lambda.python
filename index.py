from __future__ import print_function
import boto3
import logging
import os
import sys
import uuid

logger = logging.getLogger()
logger.setLevel(logging.INFO)
s3_client = boto3.client('s3')

def handler(event, context):
    logging.info("Executing main.handler")
