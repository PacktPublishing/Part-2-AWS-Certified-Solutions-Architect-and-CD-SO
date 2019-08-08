import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print ("product: " + event['product'] )
    print ("price: " + event['price'] )
    print ("currency: " + event['currency'] )

    return '{} available for {} {}'.format(event['product'],event['currency'],event['price']) # Echo back the first key value
    #raise Exception('Something went wrong')
