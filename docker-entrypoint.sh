#!/bin/sh
if [ -e requirements.txt ]
then
    pip install --no-cache-dir -r requirements.txt
fi

exec "$@"