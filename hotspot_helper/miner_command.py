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


def get_peerbook():
    raw_peerbook = run_miner_command(['peer', 'book', '-a'])
    return raw_peerbook
