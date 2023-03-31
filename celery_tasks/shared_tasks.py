import sys

from celery import shared_task

from tasks.models import Task, State

sys.set_int_max_str_digits(200000)


@shared_task
def start_task(task_id: int):
    task = Task.objects.get(id=task_id)
    task.status = State.PENDING
    task.save()


@shared_task
def fibonacci_sum(task_id: int, n: int) -> int:
    assert n > 0, 'Use a positive number'
    task = Task.objects.get(id=task_id)

    first = 0
    second = 1
    counter = 1
    if n < 2:
        return first

    total = first
    while counter < n:
        total = total + second
        first, second = second, first + second
        counter += 1

    task.status = State.READY
    task.save()
    return total


if __name__ == "__main__":
    fibonacci_sum(500000)
