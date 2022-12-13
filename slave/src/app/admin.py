from django.contrib import admin

from app.models import *

# Register your models here.
admin.site.register(Service)
admin.site.register(Workshop)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Employee)
admin.site.register(Services_order)
