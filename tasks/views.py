import logging

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic

from tasks.models import Task, State


class IndexView(generic.ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'task_list'


def status(request, task_id: int):
    logging.debug(f"Getting task {task_id} status")
    task = get_object_or_404(Task, pk=task_id)
    return HttpResponse(task.status)


def start(request, task_id: int):
    logging.debug(f"Starting task {task_id}")
    task = get_object_or_404(Task, pk=task_id)
    task.status = State.PENDING
    task.save()
    return HttpResponse("OK")