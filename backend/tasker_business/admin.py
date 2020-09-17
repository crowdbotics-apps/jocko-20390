from django.contrib import admin
from .models import TaskerAvailability, TaskerSkill, Timeslot, BusinessPhoto

admin.site.register(Timeslot)
admin.site.register(TaskerAvailability)
admin.site.register(BusinessPhoto)
admin.site.register(TaskerSkill)

# Register your models here.
