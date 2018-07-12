init:
	pipenv install --dev
	npm install serverless
	npm install serverless-python-requirements

# pytest expects that you run tests against an installed package
# there is nothing to install here I need to add the source code to PYTHONPATH
# so that the tests can be executed against the source code
integration-test:
	@PYTHONPATH=src pipenv run pytest integration-tests

package:
	@./sls package

deploy:
	@./sls deploy

# generates the config file
config:
	@echo "[default]" > config.ini

	@echo -n "api_url=" >> config.ini
	@./sls info | grep "POST.*https.*push-notifications" | cut -d' ' -f5 | cut -d'/' -f1-4 >> config.ini

smoke-test: config
	@pipenv run pytest smoke-tests

remove:
	@./sls remove
