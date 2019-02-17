#!/usr/bin/env bash

# Start persistence engine
/usr/bin/mongod --config /etc/mongodb.conf &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start MONGO: $status"
  exit $status
fi

# Start graphql server
python /opt/app.py &
status=$?
python_pid=$!
if [ $status -ne 0 ]; then
  echo "Failed to start app.py: $status"
  exit $status
fi

while true; do
  ps aux |grep /usr/bin/mongod |grep -q -v grep
  MONGO_STATUS=$?
  if [ $MONGO_STATUS -ne 0 ]; then
    echo "MongoDB has already exited."
    exit 1
  fi

  if ps -p $python_pid ; then
    echo "Python APP UP AND RUNNING"
   else
    echo "Python APP DEATH"
    exit 1
  fi

  sleep 60
done