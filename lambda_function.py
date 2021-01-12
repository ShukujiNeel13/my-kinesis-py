import json
from pprint import pformat
import base64

DEBUG = True

ATTR_NAME_RECORDS = 'Records'

EXAMPLE_TEST_EVENT = {
    "Records": [
        {
            "kinesis": {
                "partitionKey": "partitionKey-03",
                "kinesisSchemaVersion": "1.0",
                "data": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0IDEyMy4=",
                "sequenceNumber": "49545115243490985018280067714973144582180062593244200961",
                "approximateArrivalTimestamp": 1428537600
            },
            "eventSource": "aws:kinesis",
            "eventID": "shardId-000000000000:49545115243490985018280067714973144582180062593244200961",
            "invokeIdentityArn": "arn:aws:iam::EXAMPLE",
            "eventVersion": "1.0",
            "eventName": "aws:kinesis:record",
            "eventSourceARN": "arn:aws:kinesis:EXAMPLE",
            "awsRegion": "ap-southeast-1"
        }
    ]
}


def d_print(statement: str):

    if DEBUG is True:
        print(statement)


def lambda_handler(event, context):
    """"""

    print('Started lambda function execution...')

    d_print(f'In Lambda handler.')
    d_print('event is:')
    d_print(pformat(event))
    d_print(f'Type of event is: {type(event)}')
    d_print('context is:')
    d_print(context)

    d_print(f'Type of context is: {type(context)}')

    try:
        handle_event(event)
    except Exception as err:
        print('Exception occurred in this execution.')
        error = {
            'type': type(err).__name__,
            'description': str(err)
        }
        print('error is:')
        print(error)
        return dict(statusCode=500, body=json.dumps(error))
    else:
        print('Function execution complete.')
        return dict(statusCode=200, body=json.dumps('Request successful!'))


def handle_event(event: dict):
    print('In handle_event()...')

    if ATTR_NAME_RECORDS not in event:
        raise Exception(f'Required attribute: {ATTR_NAME_RECORDS} missing in received event data.')
    records = event[ATTR_NAME_RECORDS]

    no_of_records_in_event = len(records)

    d_print(f'This event contains {no_of_records_in_event} Records.')

    responses = []
    if no_of_records_in_event == 1:
        record = records[0]
        response = process_record(record)
        responses.append(response)
    else:
        for record in records:
            response = process_record(record)
            responses.append(response)


def process_record(record: dict) -> dict:
    """"""

    payload = base64.b64decode(record['kinesis']['data'])
    d_print('\nDecoded kinesis data Payload as:')
    d_print(pformat(payload))

    return {'status': 'complete'}


if __name__ == '__main__':
    dummy_context = {'name': 'test'}
    lambda_handler(event=EXAMPLE_TEST_EVENT, context=dummy_context)
