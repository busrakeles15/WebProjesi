from django.db import models
from django.utils import timezone

class IletisimModel(models.Model):
    adi = models.CharField(max_length=100)
    soyadi = models.CharField(max_length=100)
    email = models.EmailField()
    yazi = models.TextField(null=True,blank=True)
    # telefon = models.PhoneNumberField()
    zaman = models.DateTimeField(default=timezone.now)
    CH_DEGERLENDIRME = [
        ("5","Çok İyi"),
        ("4","İyi"),
        ("3","Kararsızım"),
        ("2","Kötü"),
        ("1","Çok Kötü")
        ]
    degerlendirme = models.CharField(choices=CH_DEGERLENDIRME,max_length=10)
    goruldu = models.BooleanField(default=False)

    def mavitik(self):
        self.goruldu = True
        self.save()



    def __str__(self):
        return f"{self.id}-{self.adi} {self.soyadi}-{self.email}"