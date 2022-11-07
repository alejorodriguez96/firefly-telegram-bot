#! /bin/bash -e

echo "Running Flake8..."
flake8 app

echo "Running pyDocStyle..."
pydocstyle app

echo "Running MyPy..."
mypy app

echo "Congratulations! All went well."
