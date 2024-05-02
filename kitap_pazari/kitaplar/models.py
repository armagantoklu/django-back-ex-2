from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Kitap(models.Model):
    isim = models.CharField(max_length=255)
    yazar = models.CharField(max_length=255)
    aciklama = models.TextField(blank=True, null=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)  # 1 defa olcak degismicek
    guncellenme_tarihi = models.DateTimeField(auto_now=True)  # her guncellemede deisecek
    yayin_tarihi = models.DateTimeField()

    def __str__(self):
        return self.isim


class Yorum(models.Model):
    kitap = models.ForeignKey(Kitap, on_delete=models.CASCADE, related_name='yorumlar')
    # yorum_sahibi = models.CharField(max_length=255)
    yorum_sahibi = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kullanici_yorumlari')
    yorum = models.CharField(max_length=255)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)  # 1 defa olcak degismicek
    guncellenme_tarihi = models.DateTimeField(auto_now=True)  # her guncellemede deisecek

    degerlendirme = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return str(self.degerlendirme)
