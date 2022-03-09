#!/bin/bash

set -e

CMD=$1
if [ "$#" -gt 1 ]; then
    shift
    CMD_PARAMS=$*
fi

case $CMD in

    web)
        echo "Executing WEB interface"
        gunicorn --workers=2 --bind=0.0.0.0:8000 api:__hug_wsgi__
    ;;

    cmd)
        echo "Executing command line interface"
        python api.py $CMD_PARAMS
    ;;

    *)
        echo "Required start params:"
        echo "    web: to start a web API"
        echo "    cmd: to execute the command line script"
    ;;

esac

exit 0