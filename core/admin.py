# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from core.models import School, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ('school',)
    list_display = ('first_name', 'last_name', 'school', 'is_active')
