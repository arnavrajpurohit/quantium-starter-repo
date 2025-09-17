#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
# This ensures the script stops if a command fails.
set -e

echo "Starting CI script..."

# Activate the virtual environment
# This command is cross-platform compatible for Bash environments (e.g., Git Bash, WSL, Linux).
source ./.venv/Scripts/activate

echo "Virtual environment activated."

# Execute the test suite using pytest
echo "Running pytest..."
pytest

# The `pytest` command returns an exit code of 0 for success or a non-zero code for failure.
# The 'set -e' command at the beginning ensures the script will exit with the same
# non-zero code if the pytest command fails, fulfilling the task's requirements.

echo "Tests passed successfully. Exiting with code 0."

exit 0