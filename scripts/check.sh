set -euo pipefail

uv venv --python 3.12 --allow-existing .venv
uv pip sync --python .venv/bin/python requirements-dev.lock

export PATH="$PWD/.venv/bin:$PATH"
export PYTHONPATH="$PWD/src${PYTHONPATH:+:$PYTHONPATH}"

python -c "import cortex_v6"
ruff format --check .
ruff check .
mypy
pytest -q
