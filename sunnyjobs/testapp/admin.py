from django.contrib import admin
from testapp.models import HydJobs
from testapp.models import BngJobs
from testapp.models import PuneJobs
# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class BngJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(HydJobs, HydJobsAdmin)
admin.site.register(BngJobs, BngJobsAdmin)
admin.site.register(PuneJobs, PuneJobsAdmin)
