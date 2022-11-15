from django.contrib import admin
from .models import Process, elements, dailyJkk, periodJkk, teamMember, teamoff,stopwatch



# Register your models here.
# admin.site.register(Jkk)
admin.site.register(Process)
admin.site.register(elements)

admin.site.register(dailyJkk)
admin.site.register(periodJkk)
admin.site.register(teamMember)
# admin.site.register(teamoff)
admin.site.register(stopwatch)
class dailyjkkAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('created', 'dailyprocess')
