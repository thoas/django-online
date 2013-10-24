pep8:
	flake8 online --ignore=E501,E127,E128,E124

test:
	coverage run --branch --source=online manage.py test online
	coverage report --omit=online/test*

release:
	python setup.py sdist register upload -s
