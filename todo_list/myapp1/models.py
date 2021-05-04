from django.db import models

# Create your models here.




class Test(models.Model):
    """
    stores the list of users

    """

    name = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)

    def __str__(self):
        return f"{self.name} : {self.password}"


class Items(models.Model):
    name = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    text = models.CharField(max_length = 255)

    def __str__(self):
        return self.text
