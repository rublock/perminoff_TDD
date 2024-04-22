from django.db import models


class Catalog(models.Model):
    STATUS_CHOICES = (
        ("true", "True"),
        ("false", "False"),
    )

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    read = models.CharField(
        max_length=5, choices=STATUS_CHOICES, default="false"
    )

    def __str__(self):
        return self.title
