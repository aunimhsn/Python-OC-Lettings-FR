from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    # https://stackoverflow.com/questions/43239875/how-i-can-change-the-default-table-name-in-the-admin-interface-in-django
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        db_table = 'lettings_address'

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    class Meta:
        db_table = 'lettings_letting'

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
