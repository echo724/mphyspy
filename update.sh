#!/bin/bash

git add .
git commit -m 'Update setup'
git push

rm -rf dist build mphyspy.egg-info
python setup.py sdist bdist_wheel
twine upload -u 'eunchan1001' -p 'Alslzk3574' - repository-url https://test.pypi.org/legacy/ dist / *
