init:
	pipenv install --dev
	npm install serverless
	npm install serverless-python-requirements

test:
	pipenv run pytest --capture=no

package:
	pipenv run ./sls package

deploy:
	pipenv run ./sls deploy

remove:
	./sls remove
