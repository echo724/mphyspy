#!/bin/bash

git add .
git commit -m 'Update Readme.md'
git push

rm -rf dist build mphyspy.egg-info
python setup.py bdist_wheel
python -m twine upload dist/*
