from django.contrib import admin
from .models import Module, SmartCalculator, Post, Profile

# Register your models here.
admin.site.register(Module)
admin.site.register(SmartCalculator)
admin.site.register(Post)
admin.site.register(Profile)
