#!/bin/bash
# Script to publish changes to Github

git pull
git add .
git commit -m "$*"
git push
