import json
import pyjokes


def get_joke(event, context):
    body = {
        "message": "--->>> Greetings from Github. Enjoy the jokes build here :)",
        "joke":pyjokes.get_joke()
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

