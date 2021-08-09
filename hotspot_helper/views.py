from flask import Blueprint
from flask import jsonify
from flask import request

from hotspot_helper.miner_client import get_peerbook
from hotspot_helper.miner_client import do_ping


VIEWS = Blueprint('views', __name__)


@VIEWS.route('/ping', methods=['POST'])
def ping():
    data = request.get_json()
    addr = data.get('addr')
    result = do_ping(addr)
    return jsonify(result)


@VIEWS.route('/connect', methods=['POST'])
def connect():
    return 'Not yet implemented', 501


@VIEWS.route('/peerbook', methods=['GET'])
def peerbook():
    peerbook = get_peerbook()
    return jsonify({'peers': peerbook})
