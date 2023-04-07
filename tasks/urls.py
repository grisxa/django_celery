from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# ex: /tasks/api/list/
router.register(r'list', views.TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # ex: /tasks/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /tasks/5/status/
    path('<int:task_id>/status/', views.status, name='status'),
    # ex: /task/5/start/
    path('<int:task_id>/start/', views.start, name='start'),
]
