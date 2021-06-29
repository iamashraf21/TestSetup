#!/bin/bash
echo "Starting the shell script"
# Exit immediately if a command exits with a non-zero status.
set -e
# Enable the globstar shell option
shopt -s globstar
# Make sure we are inside the github workspace
cd $GITHUB_WORKSPACE

# Link Arduino library
#ln -s $GITHUB_WORKSPACE $HOME/Arduino/libraries/CI_Test_Library
ls -l /dev/serial/by-path
whoami

cd $HOME/Documents/myagent/_work/1/s/test/
arduino-cli compile -b Seeeduino:samd:zero -e
arduino-cli upload -p /dev/ttyACM0 -b Seeeduino:samd:zero
#rm -r test-results.xml
#sleep 5
#python SerialRead.py


