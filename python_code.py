import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

fulfillment = {
    'sessionAttributes': '',
    'dialogAction': {
        'type': 'Close',
        'fulfillmentState': 'Fulfilled',
        'message': {
            'contentType': 'SSML',
            'content': '<EMPTY>'
        }
    }
}

def get_fulfillment(event, msg):
    logger.info(('Inside fulfillment.get_fulfillment()'))
    logger.debug(('Recieved msg: ', msg))
    fulfillment['sessionAttributes'] = event['sessionAttributes']
    fulfillment['dialogAction']['message']['content'] = str(msg)
    return fulfillment
