init:
	pipenv install --dev
	npm install serverless
	npm install serverless-python-requirements

test:
	pipenv run pytest tests --capture=no

package:
	pipenv run ./sls package

deploy:
	pipenv run ./sls deploy

# generates config file
config:
	# default section
	echo "[default]" > config.ini

	# push_notification_url
	echo -n "push_notification_url=" >> config.ini
	./sls info | grep "POST.*https.*push-notifications" | cut -d' ' -f5 >> config.ini

smoke-test: config
	pipenv run pytest smoke-tests

remove:
	./sls remove
