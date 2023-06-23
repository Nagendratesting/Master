#!/bin/bash

# Specify the port number
port_number="5000"

# Find the process ID (PID) associated with the port
process_id=$(lsof -t -i :"$port_number")

# Check if the process is running
if [ -z "$process_id" ]; then
  echo "No process is running on port $port_number."
  exit 1
fi

# Terminate the process
kill "$process_id"

# Check the exit status of the kill command
if [ $? -eq 0 ]; then
  echo "The process running on port $port_number (PID: $process_id) has been stopped."
else
  echo "Failed to stop the process running on port $port_number."
fi
