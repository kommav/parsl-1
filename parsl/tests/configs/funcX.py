from parsl.config import Config
from parsl.executors.funcX import FuncXExec
from parsl.executors.threads import ThreadPoolExecutor

import ssl
import pika
import certifi

# # Path to your client certificate file
client_certfile = 'client_certificate.pem'

# # Path to your client private key file
client_keyfile = 'client_key.pem'

# # Create an SSL context with certificate verification and client certificate
context = ssl.create_default_context(cafile=certifi.where())
context.load_cert_chain(certfile=client_certfile, keyfile=client_keyfile)

# Now you have a connection to the AMQP server with SSL client certificate authentication

def fresh_config():
    return Config(
        # Tutorial Endpoint should be used here, pytest should be installed on tutorial_endpoint
        executors=[FuncXExec(endpoint_id='8e7f13f5-5a89-49c6-85b4-f8929cb0d8ae', max_threads=16)],
        retries=2
    )

config = fresh_config()