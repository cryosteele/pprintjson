from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from django_mysql.models import JSONField
from .models import Variables

@admin.register(Variables)
class VariablesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

#admin.site.register(Variables, VariablesAdmin)

