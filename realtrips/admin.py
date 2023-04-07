from django.contrib import admin

from realtrips.models import Expense,  Trip, Vehicle
class TripAdmin(admin.ModelAdmin):
    list_display = ('Vehicle','odometer_start', 'odometer_close', 'journey_start','journey_destination','amount_collected')
    list_filter = ("Vehicle"),
    readonly_fields = ('total_amount_collected',)


   

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('Vehicle', 'name', 'amount_incurred','created')
    list_filter = ("Vehicle","name","amount_incurred","created")
    # readonly_fields = ('total_expense_incurred',)
    # search_fields = ['Vehicle']    


admin.site.register(Vehicle)
admin.site.register(Trip, TripAdmin)
admin.site.register(Expense,ExpenseAdmin)
# admin.site.register(Route, RouteAdmin)