from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# ex: /tasks/api/
router.register('', views.TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    # ex: /tasks/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /tasks/5/status/
    path('<int:task_id>/status/', views.status, name='status'),
    # ex: /task/5/start/
    path('<int:task_id>/start/', views.start, name='start'),
]
