import subprocess
from copy import deepcopy


CMD = ['docker', 'exec', 'miner', '/opt/miner/bin/miner']


def run_miner_command(command):
    cmd = deepcopy(CMD)
    cmd.extend(command)
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    ).stdout
    return result


def to_peer_dict(peer_list):
    peer_dict = {
        'address': peer_list[0],
        'name': peer_list[1],
        'listen': peer_list[2],
        'connection': peer_list[3],
        'nat': peer_list[4],
        'last_updated': peer_list[5]
    }
    if peer_dict['nat'] == 'symmetr':
        peer_dict['nat'] = 'symmetric'
    return peer_dict


def parse_peerbook(pb):
    # Remove the footer
    pb = pb.rsplit('|', 1)[0]
    # Remove the headers
    split = pb.split('|')
    split = split[8:]
    # Remove new lines
    split.remove('\n')
    # Trim any whitespace
    split = list(map(str.strip, split))
    split = list(filter(None, split))
    # Convert list to list of peers as lists...
    peers = [split[x:x+6] for x in range(0, len(split),6)]
    # Convert list of peers as lists to list of peers as dictionaries
    pb_dict = list(map(to_peer_dict, peers))
    return pb_dict


def get_peerbook():
    raw_peerbook = run_miner_command(['peer', 'book', '-a'])
    return parse_peerbook(raw_peerbook)
