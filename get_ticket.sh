#!/usr/bin/env bash

./wait_to_start.py

echo "Starting!!"

for (( i=0; i<10; i++ )); do
    ./load_coachella_page.py &
done
