#!/bin/bash

git add .
git commit -m 'Update setup'
git push

rm -rf dist build mphyspy.egg-info
python setup.py sdist bdist_wheel
python -m twine upload dist/*
