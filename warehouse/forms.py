from django import forms

from warehouse.models import DimensionModel, GradeModel, HeatModel


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


class GradeForm(forms.ModelForm):
    class Meta:
        model = GradeModel
        fields = ("name",)
        labels = {
            "name": "Gatunek"
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "oznaczenie"}
            )
        }


class HeatForm(forms.ModelForm):
    class Meta:
        model = HeatModel
        fields = ("name",)
        labels = {
            "name": "Wytop"
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "oznaczenie"}
            )
        }
