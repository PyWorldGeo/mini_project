from django.contrib import admin

# Register your models here.
from .models import Name, User, Type


admin.site.register(Name)
admin.site.register(User)
admin.site.register(Type)

