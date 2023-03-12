from django import forms

from schemas.models import DataSchemas


class SchemaForm(forms.ModelForm):
    class Meta:
        model = DataSchemas
        fields = "__all__"


class RowsForm(forms.Form):
    rows = forms.IntegerField()

    # title = forms.CharField(max_length=100, required=True, label="Title")
    # type_1 = forms.ChoiceField(
    #     choices=(
    #         ("full_name", "Full name"),
    #         ("phone_number", "Phone number"),
    #         ("age", "Age"),
    #         ("text", "Text"),
    #         ("email", "Email"),
    #     ),
    #     label="Type",
    # )
    # column_name_1 = forms.CharField(max_length=100, required=True, label="Column name")
    # type_2 = forms.ChoiceField(
    #     choices=(
    #         ("age", "Age"),
    #         ("phone_number", "Phone number"),
    #         ("full_name", "Full name"),
    #         ("text", "Text"),
    #         ("email", "Email"),
    #     ),
    #     label="Type",
    # )
    # column_name_2 = forms.CharField(max_length=100, required=True, label="Column name")
    # type_3 = forms.ChoiceField(
    #     choices=(
    #         ("email", "Email"),
    #         ("phone_number", "Phone number"),
    #         ("full_name", "Full name"),
    #         ("age", "Age"),
    #         ("text", "Text"),
    #     ),
    #     label="Type",
    # )
    # column_name_3 = forms.CharField(max_length=100, required=True, label="Column name")


