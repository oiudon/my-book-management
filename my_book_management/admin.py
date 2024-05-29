from django.contrib import admin

from .models import Category, ReadingList, Review

admin.site.register(Category)
admin.site.register(ReadingList)
admin.site.register(Review)
