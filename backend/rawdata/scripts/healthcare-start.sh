#!/bin/bash

SERVICE_PATH="/rawData"
SOURCE="raw_data.py"
SOURCE_PATH="$SERVICE_PATH/$SOURCE"

sudo python3 $SOURCE_PATH >/dev/null 2>&1 &
