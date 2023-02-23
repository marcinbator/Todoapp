from django.db import models
from django.contrib.auth.models import User


class Element(models.Model):
    title = models.CharField(("Tytuł"), max_length=50)
    content = models.TextField(("Zawartość"))
    done = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(
        ("Data dodania"), auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title
