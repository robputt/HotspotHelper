from flask import Blueprint
from flask import jsonify

from hotspot_helper.miner_command import get_peerbook


VIEWS = Blueprint('views', __name__)


@VIEWS.route('/ping', methods=['POST'])
def ping():
    return 'Not yet implemented', 501


@VIEWS.route('/connect', methods=['POST'])
def connect():
    return 'Not yet implemented', 501


@VIEWS.route('/peerbook', methods=['GET'])
def peerbook():
    peerbook = get_peerbook()
    return jsonify({'peers': peerbook})
