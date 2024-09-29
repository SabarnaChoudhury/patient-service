from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    diagnosis = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)
    image = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name
