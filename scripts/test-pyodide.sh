#!/usr/bin/env bash
# Run the async integration tests inside Pyodide (CPython compiled to
# WebAssembly, executed by Node). `.pyodide-venv/bin/python` *is* Pyodide, so
# everything below the install step runs with sys.platform == "emscripten";
# tests/conftest.py deselects the sync tests there.
#
# uv does not support the Emscripten platform: never `uv run`/`uv pip` inside
# .pyodide-venv, only its own pip and python.
set -euo pipefail
cd "$(dirname "$0")/.."

# The service packages tests/ imports; the root is not a package.
SERVICES=(s3 sts iam ebs ec2 transcribe-streaming)

# 1. create the Pyodide venv once
[ -d .pyodide-venv ] || uv run pyodide venv .pyodide-venv

# 2. build the service wheels (pure Python, so plain `uv build` is enough)
rm -rf dist
for service in "${SERVICES[@]}"; do
    uv build "services/$service" --wheel -o "$PWD/dist"
done

# 3. export the locked test deps. The editable service paths are replaced by
#    the wheels above; the pruned packages are host-only tools that either do
#    not build for Pyodide (trio, pytest-xdist) or are not needed to run tests.
#    msgpack (hishel's dependency) is unpinned because Pyodide ships its own
#    build of it, which is older than the locked version.
no_emit=()
for service in "${SERVICES[@]}"; do
    no_emit+=(--no-emit-package "capo-$service")
done
uv export --only-group dev --no-hashes --no-emit-project "${no_emit[@]}" \
    --prune pyodide-build --prune ty --prune ry-cli --prune pytest-xdist --prune trio --prune msgpack \
    > .pyodide-reqs.txt

# 4. install with the Pyodide venv's own pip
.pyodide-venv/bin/pip install dist/*.whl -r .pyodide-reqs.txt

# 5. run the tests inside Pyodide
.pyodide-venv/bin/python -m pytest tests "$@"
