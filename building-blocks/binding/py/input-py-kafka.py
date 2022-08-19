#dependencies
import logging
from dapr.ext.grpc import App, BindingRequest

#code
app = App()

@app.binding('checkout')
def getCheckout(request: BindingRequest):
    logging.basicConfig(level = logging.INFO)
    logging.info('Received Message : ' + request.text())

app.run(6002)
