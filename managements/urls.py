from django.urls import path, include
from .views import ExercisesListView, ExerciseDetailView

app_name = "management"
urlpatterns = [
    path(route=f"exercises/", view=ExercisesListView.as_view()),
    path(route=f"exercises/<int:pk>", view=ExerciseDetailView.as_view())
]