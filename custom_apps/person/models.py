from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
