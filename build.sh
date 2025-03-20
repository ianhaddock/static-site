#!/usr/bin/bash

echo ' >> starting src/main.sh'
python3 src/main.py https://ianhaddock.github.io/static-site/

echo ' >> starting web server'
cd public
python3 -m http.server 8888 &
echo 'PID: ' $!
