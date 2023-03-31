# Django + Celery sample application
## Running
To start the back-end run
```python manage.py runserver```
then open http://127.0.0.1/tasks/

## Using
To create or update the task use the admin app http://127.0.0.1/admin/

New tasks can be started with respective button. Pending tasks are refreshing
each 10 seconds until coming to the Ready state.

