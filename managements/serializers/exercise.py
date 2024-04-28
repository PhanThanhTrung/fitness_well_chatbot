from rest_framework import serializers
from django.utils import timezone
from ..models import Exercise

class ExerciseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=200)
    exercise_type = serializers.CharField()
    main_muscle = serializers.CharField()
    description = serializers.CharField()
    tools_required = serializers.CharField(max_length=200, allow_blank=True)
    tier = serializers.CharField(max_length=10, allow_blank=True)
    description = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Exercise` instance, given the validated data.
        """
        return Exercise.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return the `Exercise` instance, given the instance and the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.exercise_type = validated_data.get('exercise_type', instance.exercise_type)
        instance.main_muscle = validated_data.get('main_muscle', instance.main_muscle)
        instance.description = validated_data.get('description', instance.description)
        instance.tools_required = validated_data.get('tools_required', instance.tools_required)
        instance.tier = validated_data.get('tier', instance.tier)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance