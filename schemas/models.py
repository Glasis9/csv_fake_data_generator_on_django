from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.first_name } {self.last_name} ({self.username})"


class DataSchemas(models.Model):
    title = models.CharField(max_length=63)
    modified = models.DateField(auto_now=True)
    full_name = models.CharField(max_length=63, blank=True, null=True)
    age = models.CharField(max_length=63, blank=True, null=True)
    phone_number = models.CharField(max_length=63, blank=True, null=True)
    company = models.CharField(max_length=63, blank=True, null=True)
    email = models.CharField(max_length=63, blank=True, null=True)

    def __str__(self):
        return f"title: {self.title}, modified: {self.modified}"


class DataSet(models.Model):
    create_dataschemas = models.BooleanField(default=False)
    status = models.CharField(max_length=15, default="Processing")
    created = models.DateField(auto_now=True)
    rows = models.IntegerField(default=0)
    dataschema = models.ForeignKey(
        DataSchemas, on_delete=models.CASCADE, related_name="dataschemas"
    )
    url = models.CharField(max_length=350, default="")

    class Meta:
        ordering = ["created"]
