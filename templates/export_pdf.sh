#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 export_pdf.py "$@"
