#!/bin/bash

autorestart='echo "no autorestart";'

if [ "$celery_autorestart_workers" == "true" ]; then
  autorestart='/app/.venv/bin/watchmedo auto-restart --directory=/app/src --pattern=*.py --recursive --'
fi

# TODO: this `cd` doesn't feel right. It was to get the project1_be module to load right
cd /app/src


# TODO: string "project1_be" should be gotten from somewhere
cmd="${autorestart} /app/.venv/bin/celery -A project1_be worker"
echo "Celery run command ${cmd}"
eval $cmd




