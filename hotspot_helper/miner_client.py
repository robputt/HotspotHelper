from jsonrpcclient import request


JSONRPC_URL = 'http://localhost:4467'


def get_peerbook():
    response = request(JSONRPC_URL, 'peer_book', addr='all')
    return response.data.result
