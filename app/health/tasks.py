from celery import task


@task(name="add")
def add(x, y):
    return x + y
