from parsl.config import Config
from parsl.executors.funcX import FuncXExec
from parsl.executors.threads import ThreadPoolExecutor

import ssl
import pika
import certifi

# Now you have a connection to the AMQP server with SSL client certificate authentication

def fresh_config():
    return Config(
        # Tutorial Endpoint should be used here, pytest should be installed on tutorial_endpoint
        executors=[FuncXExec(endpoint_id='4b116d3c-1703-4f8f-9f6f-39921e5864df', max_threads=16)],
        retries=2
    )

config = fresh_config()