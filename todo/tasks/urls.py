from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api.resources import TaskViewSet, done


router = DefaultRouter()
router.register(r'tasks', viewset=TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:pk>/done/', done, name='task-done')
]
