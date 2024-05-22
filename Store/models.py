from django.db import models

# Create your models here.


# CUSTOMER PROFILE
class Customers(models.Model):
    full_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=20)
    address = models.TextField(null=True)

    class Meta:
        verbose_name_plural = '1. Customers'

    def __str__(self):
        return self.full_name


# CUSTOMER MEASUREMENT
class Measurement(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    len = models.CharField(max_length=10, null=True)
    waist = models.CharField(max_length=10, null=True)
    amount = models.FloatField()

    class Meta:
        verbose_name_plural = '2.Measurement'

    def __str__(self):
        return self.title
