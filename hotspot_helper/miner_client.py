from jsonrpcclient import request


JSONRPC_URL = 'http://localhost:4467'


def get_peerbook():
    response = request(JSONRPC_URL, 'peer_book', addr='all')
    return response.data.result


def do_ping(addr):
    response = request(JSONRPC_URL, 'peer_ping', addr=addr)
    result = response.data.result

    if result.get('error', None):
        return {
            'addr': addr,
            'up': False,
            'error': result.get('error')
        }

    response_time = None
    for k,v in result.items():
        response_time = v

    return {
        'addr': addr,
        'up': True,
        'latency': response_time
    }
