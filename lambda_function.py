import json
from pprint import pformat
import base64

from tests import data

DEBUG = True

PPRINT = True

ATTR_NAME_RECORDS = 'Records'


def p_print_debug_data(data: any):

    if DEBUG is False:
        return

    if PPRINT is True:
        print(pformat(data))
    else:
        print(data)


def d_print(statement: str):

    if DEBUG is True:
        print(statement)


def lambda_handler(event, context):
    """"""

    print('Started lambda function execution...')

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

    d_print('In handle_event()...')

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

    _decoded_bytes_str = base64.b64decode(record['kinesis']['data']).decode('utf-8')
    d_print('Decoded base64 string to bytes and decoded bytes to utf-8 string.')
    desired_data = json.loads(_decoded_bytes_str)
    d_print('Deserialized the json string to dictionary.')
    d_print('\nRecord data is:')
    p_print_debug_data(desired_data)

    handler_response = datahandler_process(desired_data)

    return {'status': 'complete'}


def datahandler_process(data: dict):

    d_print('Starting datahandler with given data...')


if __name__ == '__main__':
    dummy_context = {'name': 'test'}
    lambda_handler(event=data.REAL_KINESIS_DATA, context=dummy_context)
