from django import forms
from django_json_widget.widgets import JSONEditorWidget
from .models import Variables


class YourForm(forms.ModelForm):
    class Meta:
        model = Variables

        fields = ('jsonfield',)

        widgets = {
            'jsonfield': JSONEditorWidget(mode='code')
        }