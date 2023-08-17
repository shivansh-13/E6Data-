#!/bin/bash

# Start 3 engine instances in the background
python engine.py &
python engine.py &
python engine.py &

# Wait for a brief moment to ensure engines are up
sleep 2

# Run the driver program with input.txt
python driver.py input.txt

# Kill the background engine processes
pkill -f engine.py
