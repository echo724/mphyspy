build: clean
	git add .
	git commit -m 'Update setup'
	git push
	python3 setup.py sdist bdist_wheel

release: build
	twine upload -s dist/*

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	rm -rf build
	rm -rf dist
	rm -rf mphyspy.egg-info

install:
	python setup.py install
