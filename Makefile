clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
init:
	python manage.py init

upgrade:
	python manage.py db upgrade

test:
	python manage.py test

run:
	python manage.py run

shell:
	python manage.py shell

coverage:
	coverage run --source app/ -m unittest discover -s tests/

proto:
	python -m grpc_tools.protoc -I protos/ --python_out=app/rpc/ --grpc_python_out=app/rpc protos/*.proto

run-prod:
	gunicorn -b admin-web:5003 -w 2 manage:app
