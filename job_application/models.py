from django.db import models


## Create a table bluebrint with columns
class Forms(models.Model):
    fname = models.CharField(max_length=80)
    lname = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    ## Define a string to return the data when printed with an instance
    def __str__(self):
        return f"{self.fname} {self.lname}"