from django.db import models


class FullName(models.Model):
    first_name = models.CharField('FirstName', max_length=100)
    last_name = models.CharField('LastName', max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
