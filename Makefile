
build:
	python3.9 -m build

publish-pypi-test: dist
	python3.9 -m twine upload --repository testpypi dist/*