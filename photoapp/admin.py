from django.contrib import admin

# Register your models here.
from .models import Category,Photographer,Gallery,Team,Stat,Service,Package,Booking,Invoice


admin.site.register(Category)
admin.site.register(Photographer)
admin.site.register(Gallery)
admin.site.register(Team)
admin.site.register(Stat)
admin.site.register(Service)
admin.site.register(Package)
admin.site.register(Booking)
admin.site.register(Invoice)
