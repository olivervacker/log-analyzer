#!/bin/bash
# ============================================================
# === get_logs.sh - Collect authentication logs =============
# ============================================================

# Define paths
LOG_FILE="/var/log/auth.log"
OUTPUT_DIR="./data/"
OUTPUT_FILE="${OUTPUT_DIR}auth_$(date +%Y%m%d_%H%M%S).log"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo "📁 Collecting logs from $LOG_FILE..."

# Extract failed login attempts
sudo grep "Failed password" "$LOG_FILE" > "$OUTPUT_FILE"

# Count the number of lines
COUNT=$(wc -l < "$OUTPUT_FILE")

echo "✅ Found $COUNT failed login attempts"
echo "💾 Saved to: $OUTPUT_FILE"
