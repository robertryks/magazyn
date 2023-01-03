from django import forms

from warehouse.models import DimensionModel


class DimensionForm(forms.ModelForm):
    class Meta:
        model = DimensionModel
        fields = ("size",)
        labels = {
            "size": "Średnica w mm"
        }
        widgets = {
            "size": forms.TextInput(
                attrs={"placeholder": "0.00"}
            )
        }