from django.db import models

# Create your models here.

class trac_nghiem(models.Model):
    ma_cau_hoi = models.BigIntegerField(max_length=10, primary_key=True,auto_created=True,blank=False,verbose_name="Question ID")
    noi_dung_cau_hoi = models.TextField(max_length=2000, blank=False, verbose_name="Question")
    dap_an_1 = models.TextField(max_length=1000, verbose_name='Answer A', blank=False)
    dap_an_2 = models.TextField(max_length=1000, verbose_name='Answer B', blank=False)
    dap_an_3 = models.TextField(max_length=1000, verbose_name='Answer C', blank=False)
    dap_an_4 = models.TextField(max_length=1000, verbose_name='Answer D', blank=False)
    dap_an_dung = models.CharField(max_length=1, verbose_name='Correct Answer', blank=False)
    giai_thich = models.TextField(max_length=2000, verbose_name='Explanation')

    class Meta:
        ordering=['ma_cau_hoi']

    def __unicode__(self):
        return self.ma_cau_hoi