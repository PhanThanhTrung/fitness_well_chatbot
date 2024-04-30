from managements.models import Exercise
from managements.serializers import ExerciseSerializer
from rest_framework import viewsets


class ExercisesViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer