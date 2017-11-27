# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from simplemooc.courses.models import Course

class CourseAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']


admin.site.register(Course, CourseAdmin)
