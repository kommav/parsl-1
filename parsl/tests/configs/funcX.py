from parsl.config import Config
from parsl.executors.funcX import FuncXExec
from parsl.executors.threads import ThreadPoolExecutor

import ssl
import pika
import certifi


def fresh_config():
    return Config(
        # User Defined Endpoint should be used here, pytest should be installed on Defined Endpoint
        executors=[FuncXExec(endpoint_id='8e7f13f5-5a89-49c6-85b4-f8929cb0d8ae', max_threads=16)],
        retries=2
    )

config = fresh_config()