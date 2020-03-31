#!/bin/bash
cd /data/openpilot/selfdrive
export LIBGL_ALWAYS_SOFTWARE=1
PASSIVE=0 NOSENSOR=1 WEBCAM=1 ./manager.py
