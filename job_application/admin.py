from django.contrib import admin
from .models import Forms

class FormsAdmin(admin.ModelAdmin):
    list_display = ("fname", "lname", "email", "occupation")  ## Displays these column name values on the table
    search_fields = ("fname", "lname", "email")  ## Adds a search bar
    list_filter = ("date", "occupation")  ## Adds a filter
    ordering = ("-fname", )  ## Descending order
    readonly_fields = ("occupation", )  ## amkes the field uneditable

admin.site.register(Forms, FormsAdmin)
