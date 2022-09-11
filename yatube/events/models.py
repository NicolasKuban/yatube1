from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Events(models.Model):
    contact = models.EmailField()
    location = models.TextField(max_length=400)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name="events")