#!/bin/bash

# Production startup script for Render
echo "Starting Ada Converter API..."

# Use gunicorn for production
exec gunicorn app.main:create_app() \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 2 \
    --timeout 120 \
    --keep-alive 2 \
    --max-requests 1000 \
    --max-requests-jitter 100 \
    --access-logfile - \
    --error-logfile -