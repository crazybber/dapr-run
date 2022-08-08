#dependencies
from dapr.clients import DaprClient
from dapr.clients.grpc._state import StateItem

#code
logging.basicConfig(level = logging.INFO)
DAPR_STORE_NAME = "statestore"
orderId = 100
#Using Dapr SDK to save and retrieve multiple states
with DaprClient() as client:
    client.save_bulk_state(store_name=DAPR_STORE_NAME, states=[StateItem(key="order_2", value=str(orderId))])
    result = client.get_bulk_state(store_name=DAPR_STORE_NAME, keys=["order_1", "order_2"], states_metadata={"metakey": "metavalue"}).items
    logging.info('Result after get bulk: ' + str(result)) 