# Django + Celery sample application
## Running
To start the back-end run
```python manage.py runserver```
then open http://127.0.0.1/tasks/

RabbitMQ must be running:
```docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management```

As the Celery itself:
```celery -A tasks worker --loglevel=INFO```

## Using
To create or update the task use the admin app http://127.0.0.1/admin/

New tasks can be started with respective button. Pending tasks are refreshing
each 10 seconds until coming to the Ready state.

