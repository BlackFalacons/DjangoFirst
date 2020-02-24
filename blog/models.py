from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150,verbose_name='Başlık')
    content = models.CharField(max_length=200,verbose_name='İcerik')
    publishing_date = models.DateTimeField(auto_now=True,verbose_name='Yayınlanma Tarihi')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishing_date']

