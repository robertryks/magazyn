from django import forms

from warehouse.models import DimensionModel, GradeModel, HeatModel, CertificateModel, SupplyModel, SupplyItemModel


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
            "name": forms.TextInput
        }


class HeatForm(forms.ModelForm):
    class Meta:
        model = HeatModel
        fields = ("name",)
        labels = {
            "name": "Wytop"
        }
        widgets = {
            "name": forms.TextInput
        }


class CertificateForm(forms.ModelForm):
    class Meta:
        model = CertificateModel
        fields = ("name",)
        labels = {
            "name": "Certyfikat"
        }
        widgets = {
            "name": forms.TextInput
        }


class SupplyForm(forms.ModelForm):
    class Meta:
        model = SupplyModel
        fields = ("number", "date",)
        labels = {
            "number": "Numer WZ",
            "date": "Data WZ"
        }
        widgets = {
            "number": forms.TextInput,
            "date": forms.DateInput(format='%Y-%m-%d')
        }


class SupplyItemForm(forms.ModelForm):
    dimension = forms.ModelChoiceField(queryset=DimensionModel.objects.all()),
    grade = forms.ModelChoiceField(queryset=GradeModel.objects.all()),
    heat = forms.ModelChoiceField(queryset=HeatModel.objects.all()),
    certificate = forms.ModelChoiceField(queryset=CertificateModel.objects.all()),
    quantity = forms.DecimalField

    class Meta:
        model = SupplyItemModel
        exclude = ("can_modify", "actual")
        labels = {
            "dimension": "Średnica",
            "grade": "Gatunek",
            "heat": "Wytop",
            "certificate": "Certyfikat",
            "quantity": "Ilość",
        }

