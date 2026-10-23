#!/bin/bash
set -e
DOSSIER_PROJET=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)

if [ -d "${DOSSIER_PROJET}/mirror-env" ] ; then
    echo "L'environnement virtuel existe déjà"
else
    python3 -m venv "${DOSSIER_PROJET}/mirror-env"
fi

"${DOSSIER_PROJET}/mirror-env/bin/python" -m pip install -r "${DOSSIER_PROJET}/requirements.txt"