from django.db import models

# Create your models here.

#Employee Model
class Employee(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=50)
    esal=models.FloatField()

    # def __str__(self):
    #     return f"{self.eid}--{self.ename}"


