#!/bin/bash

# The part that asks the user whether to install an API key.
read -p "Would you like to install an API key? (Y/N) " response

# Convert input values to lowercase to process them case-insensitively.
response=$(echo $response | tr '[:upper:]' '[:lower:]')

# Conditional branching
if [[ "$response" == "y" ]]; then
    echo "Install your API key."
    # API 키 설치 로직을 여기에 추가
elif [[ "$response" == "n" ]]; then
    echo "Skip API key installation."
else
    echo "Invalid input. Please enter Y or N."
fi
