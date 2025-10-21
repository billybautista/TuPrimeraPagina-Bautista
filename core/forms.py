from django import forms
from .models import Owner, Pet


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ["name", "email", "phone"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Nombre"}),
            "email": forms.EmailInput(attrs={"placeholder": "email"}),
            "phone": forms.TextInput(attrs={"placeholder": "celular"}),
        }


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "age", "breed", "pet_type", "owner"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Nombre"}),
            "age": forms.NumberInput(attrs={"placeholder": "Edad"}),
            "breed": forms.TextInput(attrs={"placeholder": "Raza"}),
        }
