#!/bin/bash

# Check if parallel command is installed
if command -v parallel &> /dev/null
then
    echo "parallel is already installed."
else
    # Install parallel
    echo "Installing parallel..."
    sudo apt-get update
    sudo apt-get install -y parallel
    echo "parallel installed successfully."
fi

# Function to check if the number is between 2 and 32
function check_number() {
    local num="$1"
    if [[ "$num" -ge 2 && "$num" -le 32 ]]; then
        return 0
    else
        return 1
    fi
}

# Check if number and file are provided as command line arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <number (2-32)> <number> <tld>"
    exit 1
fi

number="$1"
file="$2.txt"
extension="$3"

# Validate the number
if ! check_number "$number"; then
    echo "Error: Domain name length must be between 2 and 32."
    exit 1
fi

# Check if the file exists
if [ ! -f "$file" ]; then
    echo "Error: File not found - $file"
    exit 1
fi

# Use parallel to run python3 check_whois.py for each word in the file
cat "$file" | parallel -j0 python3 check_whois.py {}.$extension
