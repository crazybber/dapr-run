#dependencies
import random
from time import sleep    
import requests
import logging
from dapr.clients import DaprClient
from dapr.clients.grpc._state import StateItem
from dapr.clients.grpc._request import TransactionalStateOperation, TransactionOperationType

#code
logging.basicConfig(level = logging.INFO)
DAPR_STORE_NAME = "statestore"
while True:
    sleep(random.randrange(50, 5000) / 1000)
    orderId = random.randint(1, 1000)
    with DaprClient() as client:
        #Using Dapr SDK to save and get state
        client.save_state(DAPR_STORE_NAME, "order_1", str(orderId)) 
        result = client.get_state(DAPR_STORE_NAME, "order_1")
        logging.info('Result after get: ' + result.data.decode('utf-8'))