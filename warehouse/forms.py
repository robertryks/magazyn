from django import forms

from warehouse.models import Dimension


class DimensionForm(forms.ModelForm):
    class Meta:
        model = Dimension
        fields = ("size",)
        labels = {
            "size": "Średnica w mm"
        }
        widgets = {
            "size": forms.TextInput(
                attrs={"placeholder": "0.00"}
            )
        }