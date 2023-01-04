from django import forms

from warehouse.models import DimensionModel


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Login')
    password = forms.CharField(max_length=63, label='Hasło', widget=forms.PasswordInput)


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