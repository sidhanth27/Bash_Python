#!/bin/bash

# Read input numbers
echo "Enter the numerator:"
read numerator

echo "Enter the denominator:"
read denominator

# Perform division
result=$((numerator / denominator))

# Output the result
echo "Result: $result"
