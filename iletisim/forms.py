from django import forms
from .models import IletisimModel
import WebSitesi.settings as setting

class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = (
            "adi",
            "soyadi",
            "email",
            "yazi",
            "degerlendirme")
        if setting.LANGUAGE_CODE == 'tr':
            labels = {
                "adi":("Adınız"),
                "soyadi":("Soyadı"),
                "email":("E Posta"),
            }
        
