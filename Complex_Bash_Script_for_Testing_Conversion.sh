#!/bin/bash

# Complex Bash Script for Testing Python Conversion

# Function to log messages
log_message() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" >> script_log.txt
}

# Error handling function
handle_error() {
    echo "ERROR: $1" >&2
    log_message "Error: $1"
    exit 1
}

# Create a temporary working directory
WORK_DIR=$(mktemp -d) || handle_error "Could not create temporary directory"
cd "$WORK_DIR" || handle_error "Could not change to working directory"

# Initialize log file
touch script_log.txt || handle_error "Could not create log file"

# System and environment information gathering
log_message "Script started"
log_message "Hostname: $(hostname)"
log_message "Current User: $(whoami)"
log_message "System Info: $(uname -a)"

# File operations demonstration
echo "Creating sample files for processing"
for i in {1..5}; do
    echo "Sample content $i" > "sample_file_${i}.txt"
done

# Text processing with multiple commands
echo "Performing text processing operations"
cat sample_file_*.txt | sort | uniq > processed_files.txt
wc -l processed_files.txt >> script_log.txt

# Network-related command simulation
echo "Simulating network-related operations"
# Ping a known reliable host
ping -c 4 google.com > ping_results.txt 2>&1 || log_message "Ping failed"

# Process manipulation and background job
(
    for j in {1..10}; do
        echo "Background process iteration $j"
        sleep 1
    done
) & 

# Mathematical operations
MATH_RESULT=$((15 * 7 + 22))
echo "Mathematical calculation result: $MATH_RESULT" >> script_log.txt

# Conditional logic
if [ $MATH_RESULT -gt 100 ]; then
    log_message "Math result is greater than 100"
else
    log_message "Math result is less than or equal to 100"
fi

# File system operations
echo "Performing file system operations"
mkdir -p "$WORK_DIR/subfolder"
cp sample_file_*.txt "$WORK_DIR/subfolder/"

# Generate some random data
head -c 1000 /dev/urandom | base64 > "$WORK_DIR/random_data.bin"

# JSON-like output demonstration
echo '{
    "script_name": "Complex Bash Test Script",
    "timestamp": "'$(date +%s)'",
    "files_processed": 5,
    "random_seed": "'$RANDOM'"
}' > script_metadata.json

# Final logging and cleanup
log_message "Script completed successfully"

# Print contents of log file
cat script_log.txt

# Optional: Clean up (commented out for demonstration)
# rm -rf "$WORK_DIR"

echo "Script execution completed. Check script_log.txt for details."