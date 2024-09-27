#!/bin/sh

if [ "$ENVIRONMENT" = "production" ]; then
    echo "Running in production mode"
    exec poetry run gunicorn -c gunicorn.conf.py
elif [ "$ENVIRONMENT" = "development" ]; then
    echo "Running in development mode"
    exec make server-container-with-content
else
    echo "ENVIRONMENT variable is not set"
fi