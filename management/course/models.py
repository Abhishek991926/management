from django.db import models

# Create your models here.
class Orgdetail(models.Model):
    name=models.CharField(max_length=70,unique=True)
    register_on=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Empdetail(models.Model):
    name=models.CharField(max_length=50,unique=True)
    orgdetail=models.ForeignKey(Orgdetail, on_delete=models.CASCADE)
    register_on=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name