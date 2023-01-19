from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    # change the return method to show it as a string
    def __str__(self):
        return self.name+' '