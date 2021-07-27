from django.contrib import admin
from .models import Mechanic,Rating,Location,Profile

# Register your models here.
admin.site.register(Mechanic)
admin.site.register(Rating)
admin.site.register(Location)
admin.site.register(Profile)

