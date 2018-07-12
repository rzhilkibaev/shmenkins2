init:
	pipenv install --dev
	npm install serverless
	npm install serverless-python-requirements

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
