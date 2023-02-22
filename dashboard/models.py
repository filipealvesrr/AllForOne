from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Caso(models.Model):
    title_of_case = models.CharField(max_length=100)
    description = models.TextField()
    value_total = models.FloatField()
    value_received = models.FloatField()
    date_expiration = models.DateField()
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True, default=None,
    )
    usuario = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title_of_case


class Donate(models.Model):
    value_of_donate = models.FloatField()
    date_of_donate = models.DateField()
    caso = models.ForeignKey(
        Caso, on_delete=models.SET_NULL, null=True
    )
    usuario = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )


class Score(models.Model):
    value_of_score = models.IntegerField()
    donate = models.ForeignKey(
        Donate, on_delete=models.SET_NULL, null=True
    )
    usuario = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
