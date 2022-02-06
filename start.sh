#!/usr/bin/env bash

nohup python3 $(dirname $0)/sensor.py &>/dev/null &
