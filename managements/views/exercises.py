from managements.models import Exercise
from managements.serializers import ExerciseSerializer
from rest_framework import generics


class ExercisesListView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer