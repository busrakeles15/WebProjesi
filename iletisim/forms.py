from django import forms
from .models import IletisimModel

class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = (
            "adi",
            "soyadi",
            "email",
            "yazi",
            "degerlendirme")
