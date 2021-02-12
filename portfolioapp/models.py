from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="project_thumbnails")
    link = models.URLField(unique=True, max_length=128)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=64)
    link = models.CharField(max_length=128)
    url = models.BooleanField(default=False)

    def __str__(self):
        return self.name
