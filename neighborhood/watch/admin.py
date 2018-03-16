from django.contrib import admin
from .models import Profile

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    filter_horizontal =()

admin.site.register(Profile)
