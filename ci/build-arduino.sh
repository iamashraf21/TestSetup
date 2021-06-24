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

echo "Printing pwd"
pwd
echo "listing files---"
ls -Rlh
#cd $HOME/work/1/s/arduino_sketch_devops
arduino-cli compile -b Seeeduino:samd:zero -e
