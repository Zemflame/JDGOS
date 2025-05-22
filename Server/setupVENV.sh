#!/bin/bash
rm -rf venv/
python3.13 -m venv venv/
venv/bin/pip install -U pip
venv/bin/pip install -U discord.py