from django import forms

from schemas.models import DataSchemas


class SchemaForm(forms.ModelForm):
    class Meta:
        model = DataSchemas
        fields = "__all__"


class RowsForm(forms.Form):
    rows = forms.IntegerField()
