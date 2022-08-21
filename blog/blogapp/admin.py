from django.contrib import admin
from .models import Restaurant, Country, City, Post

# Register your models here.

admin.site.register([Restaurant, Country, City, Post])