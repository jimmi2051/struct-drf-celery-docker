build:
	cd app && docker build -t deftnt .

start:
	docker-compose -p deftnt up -d

restart:
	docker-compose -p deftnt restart

reset:
	docker-compose -p deftnt down

	docker-compose -p deftnt up -d

stop:
	docker-compose -p deftnt stop

down:
	docker-compose -p deftnt down

down_v:
	docker-compose -p deftnt down -v

migrate:
	docker exec -it deftnt_app_1 pipenv run python3 manage.py migrate

coverage_test:
	docker exec -it deftnt_app_1 pipenv run coverage run manage.py test

coverage_report:
	docker exec -it deftnt_app_1 pipenv run coverage report

coverage_view:
	docker exec -it deftnt_app_1 pipenv run coverage html

test:
	docker exec -it deftnt_app_1 pipenv run python3 manage.py test
