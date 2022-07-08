build:
	cd app && docker build -t app .

start:
	docker-compose -p app up -d

restart:
	docker-compose -p app restart

reset:
	docker-compose -p app down

	docker-compose -p app up -d

stop:
	docker-compose -p app stop

down:
	docker-compose -p app down

down_v:
	docker-compose -p app down -v

migrate:
	docker exec -it app_app_1 pipenv run python3 manage.py migrate

coverage_test:
	docker exec -it app_app_1 pipenv run coverage run manage.py test

coverage_report:
	docker exec -it app_app_1 pipenv run coverage report

coverage_view:
	docker exec -it app_app_1 pipenv run coverage html

test:
	docker exec -it app_app_1 pipenv run python3 manage.py test
