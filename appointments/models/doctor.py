from django.db import models

class Doctor(models.Model):
    name             = models.CharField(max_length = 30)
    first_last_name  = models.CharField(max_length = 30)
    second_last_name = models.CharField(max_length = 30)
    birthday         = models.DateTimeField()
    speciality       = models.CharField(max_length = 100)

    class Meta:
        db_table = 'doctor'

    def __str__(self):
        return f"{self.name} {self.first_last_name} {self.second_last_name}"