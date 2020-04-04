from django.db import models
from django.utils import timezone

class BlogModel(models.Model):
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    SECENEKLER = [
        ("1","Düz Yazı"),
        ("2","Günlük")
    ]
    tip = models.CharField(choices=SECENEKLER,max_length=10)
    yayim_tarihi = models.DateTimeField(null=True,blank=True)
    kayit_tarihi = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.baslik
    