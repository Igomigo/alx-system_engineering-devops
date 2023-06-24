#!/usr/bin/python3
"""
Script that commits a file to my github repository
"""

from sys import argv


git add .
git commit -m "argv[1:]"
git push
