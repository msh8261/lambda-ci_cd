import json
import pyjokes


def get_joke(event, context):
    body = {
        "message": "Greetings from Github. This is a fun please enjoy the jokes provided here",
        "joke":pyjokes.get_joke()
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

