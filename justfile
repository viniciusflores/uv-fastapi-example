help:
  just --list

sync:
  uv sync


test:
  uv run coverage run -m pytest -n 20 -s -v
