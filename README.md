# Struct source DRF + Celery + Redis in Docker-compose

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

**_This is instructions based on OS: Ubuntu v18.04_**

- **Docker** version >= 19.03.5
  . `sudo apt-get install docker`
- **Docker-compose** version >= 1.25.4
  . `sudo apt-get install docker-compose`

### Installing

**_Prepare variable environment_**

1. Rename the file **_.env.sample_** to **_.env_**
1. Update value of variable in file **_.env_**

**_Run docker-compose_**

```
docker-compose up --build -d
```

1. HealthCheck
   Acccess to: http://localhost:8000/api/v1/healthCheck will be received response as

```
{
  "description": "the service is healthy"
}
```

2. Test Celery:
   Acccess to: http://localhost:8000/api/v1/testCelery will be received response as

```
{
  "task_id": "f14e3eb8-b496-4705-b417-5620308d4ab7",
  "status": "ok"
}
```

3. Test S3 Config:
   Acccess to: http://localhost:8000/api/v1/testS3Config will be received response as

```

{
  "status": "Ok",
  "buckets": [
    "bucket-name-1",
    "bucket-name-2"
  ]
}
```

## Running the tests

**_Run Unit test & Performance test_**

```
1. docker exec -it <folder-name>_app_1 bash # Attach Shell to container web
2. pipenv shell # Active environment
3. python manage.py test # Run test case
```

**_Run Coverage Test_**

```
1. docker exec -it <folder-name>_app_1 bash # Attach Shell to container web
2. pipenv shell # Active environment
3. coverage run manage.py test # Run test case by coverage
(Optional: View By HTML) coverage html
(Optional: View Report) coverage report
```

## Deployment

**_Updating ..._**

## Contributing

1. Install new package

```
1. rm -rf Pipfile.lock # Remove Pipfile.lock
2. docker exec -it <folder-name>_app_1 bash # Attach Shell to container web
3. pipenv shell # Active environment
4. pipenv install <package-name> # Install new package
5. pipenv install # Generate new Pipfile.lock
```

## Versioning

0.1.0

## Authors

- **Thanh Nguyen Ly** - _Initial work_ - [thanhngly](https://github.com/jimmi2051) - [thanhnl0697@gmail.com]()

## License

<!-- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details -->
