#!/bin/sh
if [ -e config/requirements.txt ]
then
    uv add -r config/requirements.txt
fi

exec "$@"