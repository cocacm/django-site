from django.contrib import admin
from .models import Blog

# register the blog app for use in the admin portal
admin.site.register(Blog)