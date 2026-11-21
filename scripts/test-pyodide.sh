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
SERVICES=(s3 sts iam ebs ec2 eventbridgev2 transcribe-streaming bedrock-runtime iot-jobs-data-plane
    amp application-auto-scaling apprunner bedrock cloudwatch cloudwatchomni cognito-identity-provider
    elasticache partnercentral-channel partnercentral-revenue-measurement route-53 sqs sso-oidc sustainability)

# Pinned: `pyodide venv` otherwise takes the newest release. 314.0.8 stopped
# asyncio.new_event_loop() from replacing the running loop (pyodide#6342), which
# breaks anyio's pytest runner ("future belongs to a different loop").
PYODIDE_VERSION=314.0.7

# 1. create the Pyodide venv once
if [ ! -d .pyodide-venv ]; then
    uv run pyodide xbuildenv install "$PYODIDE_VERSION"
    uv run pyodide venv .pyodide-venv
fi

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
    --prune pyodide-build --prune ty --prune ry-cli --prune ruff --prune pytest-xdist --prune trio --prune msgpack \
    > .pyodide-reqs.txt

# 4. install with the Pyodide venv's own pip
.pyodide-venv/bin/pip install dist/*.whl -r .pyodide-reqs.txt

# 5. run the tests inside Pyodide
.pyodide-venv/bin/python -m pytest tests "$@"
