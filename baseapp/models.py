from django.db import models


class Element(models.Model):
    title = models.CharField(("Tytuł"), max_length=50)
    content = models.TextField(("Zawartość"))
    date = models.DateTimeField(
        ("Data dodania"), auto_now_add=True)
