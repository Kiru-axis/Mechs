from django.contrib import admin
from .models import Mechanic,Rating,Location,Profile,Comment

# Register your models here.
admin.site.register(Mechanic)
admin.site.register(Rating)
admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(Comment)

