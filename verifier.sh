#!/bin/bash
set -e

DOSSIER_PROJET=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)

"${DOSSIER_PROJET}/mirror-env/bin/python" -m pytest "${DOSSIER_PROJET}/tests"

"${DOSSIER_PROJET}/mirror-env/bin/python" -m ruff check "${DOSSIER_PROJET}/modules" "${DOSSIER_PROJET}/tests"

"${DOSSIER_PROJET}/mirror-env/bin/python" -m ruff format  --check "${DOSSIER_PROJET}/modules" "${DOSSIER_PROJET}/tests"

"${DOSSIER_PROJET}/mirror-env/bin/python" -m mypy --disable-error-code=import-untyped "${DOSSIER_PROJET}/modules"