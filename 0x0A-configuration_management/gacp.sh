#!/bin/bash
# script that commits a change to my github repository

message="$1"

git add .
git commit -m "$message"
git push
