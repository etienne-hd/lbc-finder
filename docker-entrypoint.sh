#!/bin/sh
if [ -e config/requirements.txt ]
then
    pip install --no-cache-dir -r config/requirements.txt
fi

exec "$@"