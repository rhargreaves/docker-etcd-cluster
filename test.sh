#!/usr/bin/env bash
set -e

echo "Upgrading pip and installing requirements..."
python3 -m pip install --upgrade pip
pip install -r requirements.txt

echo "Bringing up the environment..."
docker compose up -d

echo "Waiting for services to start..."
sleep 5

echo "Running tests..."
python3 -m pytest -v test/etcd-test.py

echo "Tests completed successfully!"
docker compose down
docker compose rm -f