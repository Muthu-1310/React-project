from django.db import models

class employee(models.Model):
    id=models.IntegerField(primary_key=True),
    name=models.CharField(max_length=30,null=True)
    age=models.IntegerField(0)
    mail=models.EmailField()



def __str__(self):
        return self.name