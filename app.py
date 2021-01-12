import sys


def handler(event, context) -> str:
    print(f'In Lambda handler.')
    print('event is:')
    print(event)
    print(f'Type of event is: {type(event)}')
    print('context is:')
    print(context)
    print(f'Type of context is: {type(context)}')

    return f'Hello from AWS Lambda Container Python {sys.version}'

