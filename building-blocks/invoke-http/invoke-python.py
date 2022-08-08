import random
import logging
from time import sleep
from dapr.clients import DaprClient

#code
logging.basicConfig(level = logging.INFO) 
while True:
    sleep(random.randrange(50, 5000) / 1000)
    orderId = random.randint(1, 1000)
    with DaprClient() as daprClient:
        #Using Dapr SDK to invoke a method
        result = daprClient.invoke_method(
            "checkout",
               f"checkout/{orderId}",
               data=b'',
               http_verb="GET"
        )    
    logging.basicConfig(level = logging.INFO)
    logging.info('Order requested: ' + str(orderId))
    logging.info('Result: ' + str(result))