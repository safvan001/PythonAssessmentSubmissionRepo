from django.db import models


class Github(models.Model):
    repo_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    stars = models.IntegerField()
    forks = models.IntegerField()
    html_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Create your models here.
