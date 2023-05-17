from konnector.sideb import redis_client
import datetime
ENDPOINT_LIST_NAME = f'endpoint:${0}:time'


def endpoint_metrics(endpoint: str = None):
    endpoint_list_name = ENDPOINT_LIST_NAME.format(endpoint)
    now = datetime.datetime.now()
    str_now = f'{now:%m/%d/%Y %H:%M:%S}'
    print(f'Adding to endpoint: {endpoint_list_name}, {str_now}')
    pushed = redis_client.rpush(endpoint_list_name, str_now)
    if pushed:
        print('All good')
    else:
        print('Error')