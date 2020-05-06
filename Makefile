build: clean
	git add .
	git commit -m 'Add conversion'
	git push
	python setup.py bdist_wheel

release: build
	python -m twine upload dist/*

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	rm -rf build
	rm -rf dist
	rm -rf mphyspy.egg-info

install:
	python setup.py install
