from django import forms

from .models import Catalog


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = "__all__"

        widgets = {
            "title": forms.fields.TextInput(attrs={"class": "form-control"}),
            "author": forms.fields.TextInput(attrs={"class": "form-control"}),
            "read": forms.fields.Select(
                attrs={"class": "form-control"}
            ),
        }
