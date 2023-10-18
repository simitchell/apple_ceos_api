from django.db import models

# Create your models here.
class AppleCeo(models.Model):
    name = models.CharField(max_length=80)
    slug = models.CharField(max_length=256)
    year = models.IntegerField()

    def __str__(self):
        #  string for representing the model object
        return self.name