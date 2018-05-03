from django.db import models
from django.utils import timezone


class Transfer(models.Model):
    author = models.ForeignKey('auth.User')
    money = models.CharField(max_length=200)
    money_off = models.CharField(max_length=200, default='')
    date_off = models.DateTimeField(default=timezone.now)
    FRESHMAN = 'Standart'
    SOPHOMORE = 'Normal'
    JUNIOR = 'Premium'
    SENIOR = 'Platinum'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Standert'),
        (SOPHOMORE, 'Normal'),
        (JUNIOR, 'Premium'),
        (SENIOR, 'Platinum'),
    )
    year_in_school = models.CharField(max_length=10,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN)

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.money
