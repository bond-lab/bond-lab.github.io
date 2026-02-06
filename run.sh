#!/bin/bash
set -e

# Ensure uv is installed
if ! command -v uv &>/dev/null; then
  echo "uv not found. Please install it first: https://github.com/astral-sh/uv"
  exit 1
fi

# Create the virtual environment if missing
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  uv venv .venv
fi

echo "Installing dependencies..."
uv pip install -r requirements.txt

echo "Starting development server..."
uv run python wsgi.py
