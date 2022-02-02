#!/bin/bash
set -x

bin/setup.sh
python slack-download.py
