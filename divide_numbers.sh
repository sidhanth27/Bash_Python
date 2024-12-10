#!/bin/bash

# Set default values
numerator=${1:-10}     # Default numerator is 10
denominator=${2:-2}    # Default denominator is 2

# Perform division
result=$((numerator / denominator))

# Output the result
echo "Numerator: $numerator"
echo "Denominator: $denominator"
echo "Result: $result"
