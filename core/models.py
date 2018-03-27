# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class School(Timestamp):
    name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name


class Student(Timestamp):
    first_name = models.CharField(null=False, blank=False, max_length=255)
    last_name = models.CharField(null=False, blank=False, max_length=255)
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
