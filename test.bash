#!/bin/bash

echo "Start Python tests"

python3 -m unittest -v test_text_cleaner.py

if [ $? -eq 0 ]; then
    echo "All tests passed!"
else
    echo "Test failed!"
    exit 1
fi
