from django.db import models

class reservemodel2(models.Model):
    checkin = models.CharField(max_length=50,verbose_name='チェックイン')
    time1 = models.CharField(max_length=50,verbose_name='開始')
    checkout = models.CharField(max_length=50,verbose_name='チェックアウト')
    time2 = models.CharField(max_length=50,verbose_name='終了')
    category=models.CharField(max_length=50,verbose_name='予約可能部屋')

    def __str__(self):
        return self.checkin