from django.db import models
from django.utils import timezone

class Exercise(models.Model):
    name = models.CharField(max_length= 200, blank=False)
    exercise_type = models.CharField(max_length=200, blank=True)
    main_muscle = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)
    tools_required = models.CharField(max_length=200, blank=True)
    tier = models.CharField(max_length=10, blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
