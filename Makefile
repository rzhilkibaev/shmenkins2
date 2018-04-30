init:
	pipenv install --dev
	npm install serverless
	npm install serverless-python-requirements

test:
	@pipenv run pytest tests --capture=no

package:
	@./sls package

deploy:
	@./sls deploy

# generates the config file
config:
	@echo "[default]" > config.ini

	@echo -n "push_notification_url=" >> config.ini
	@./sls info | grep "POST.*https.*push-notifications" | cut -d' ' -f5 >> config.ini

smoke-test: config
	@pipenv run pytest smoke-tests

remove:
	@./sls remove
