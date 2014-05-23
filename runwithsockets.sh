#!/usr/bin/env bash

echo "Make sure you're sourced in the virtualenv before launching that."
gunicorn -k flask_sockets.worker app:app