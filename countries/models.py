from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=2, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name
