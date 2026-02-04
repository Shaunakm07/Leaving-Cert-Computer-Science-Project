#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   bash run_pipeline.sh 30
#   ./run_pipeline.sh 30
#
# If no argument is given, defaults to 30 seconds.
DURATION="${1:-30}"

RAW_CSV="serial_raw_data.csv"
CLEAN_CSV="serial_cleaned_data.csv"
PARSED_CSV="serial_parsed_only.csv"

# Use the currently-active Python (e.g., your conda env's python)
PYTHON="$(command -v python || true)"
if [[ -z "${PYTHON}" ]]; then
  PYTHON="$(command -v python3)"
fi

echo "Using Python: $PYTHON"
"$PYTHON" -c "import sys; print('Python executable:', sys.executable)"

echo "=== Deleting old CSV files (if any) and creating fresh ones ==="
for f in "$RAW_CSV" "$CLEAN_CSV" "$PARSED_CSV"; do
  rm -f "$f"
  : > "$f"
  echo "Fresh file created: $f"
done

echo "=== Running read_serial.py for ${DURATION} seconds ==="
"$PYTHON" read_serial.py &
PID=$!

sleep "$DURATION"

echo "Stopping read_serial.py (PID $PID)..."
kill "$PID" 2>/dev/null || true
wait "$PID" 2>/dev/null || true

echo "=== Running parse_csv.py ==="
"$PYTHON" parse_csv.py

echo "=== Running plot_serial_data.py ==="
"$PYTHON" plot_serial_data.py

echo "=== Done ==="
