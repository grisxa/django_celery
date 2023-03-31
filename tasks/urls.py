from django.urls import path

from . import views

urlpatterns = [
    # ex: /tasks/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /tasks/5/status/
    path('<int:task_id>/status/', views.status, name='status'),
    # ex: /task/5/start/
    path('<int:task_id>/start/', views.start, name='start'),
]
