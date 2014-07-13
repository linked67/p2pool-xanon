#!/bin/sh
SERVICE='python ./run_p2pool.py --net xanon'

if ps ax | grep -v grep | grep "$SERVICE" > /dev/null
then
        echo "$SERVICE is already running!"
else
        screen  -m -S screenxanon python ./run_p2pool.py --net xanon --give-author 0 --disable-upnp -f 1 -a LctfsTWpNqLLPwTmcZ1G5DyASMQnf7zjWw

	wait
fi
