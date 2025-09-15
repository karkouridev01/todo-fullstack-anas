from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=150)
    done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
