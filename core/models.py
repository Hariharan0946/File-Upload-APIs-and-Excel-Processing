from django.db import models

class UserRecord(models.Model):
    excel_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    education = models.CharField(max_length=100)

    def __str__(self):
        return self.name
