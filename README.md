# Hotspot Helper Service

## Prerequisites
- Python 3.6 or newer
- Docker

## Quick Start
Create Python3 VirtualEnv and Install Dependencies
```bash
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

Start the Miner Docker Container
```bash
mkdir miner_data
docker pull quay.io/team-helium/miner:latest-amd64
docker run --volume miner_data:/var/data --name miner quay.io/team-helium/miner:latest-amd64
```

Run the API
```bash
export PYTHONPATH=`pwd` python3 hotspot_helper/app.py
```
