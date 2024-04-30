from django.urls import path, include
from .views import ExercisesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(prefix=r"exercises/", viewset=ExercisesViewSet, basename="exercise")

urlpatterns = [
    path('', include(router.urls)),
]