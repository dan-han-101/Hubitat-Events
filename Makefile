
# Build the distribution package. See generated files in `dist/`.
build:
	python3.9 -m build

publish-pypi-test: dist
	python3.9 -m twine upload --repository testpypi dist/*

test:
	python3.9 -m pytest
