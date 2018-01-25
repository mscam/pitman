.PHONY: test install pep8 release clean

test: pep8
	py.test -l --tb=short --maxfail=1

install:
	python setup.py develop

pep8:
	@flake8 program --ignore=F403 --exclude=junk

release: test
	@python setup.py sdist bdist_wheel upload

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
