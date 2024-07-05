#!/bin/bash
/app/.venv/bin/python /app/src/manage.py migrate && \
  /app/.venv/bin/python /app/src/manage.py runserver 0.0.0.0:7665
