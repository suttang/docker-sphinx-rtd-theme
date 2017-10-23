#!/bin/sh
set -euo pipefail

SCRIPT_DIR=$(cd $(dirname $0); pwd)

if [ "$1" == "sphinx-quickstart" ]; then
    shift
    exec python $SCRIPT_DIR/quickstart.py "$@"
fi

exec "$@"
