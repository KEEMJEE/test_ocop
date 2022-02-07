from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Carbonpoint(models.Model):
    pointtype = models.TextField()
    cpoint = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    # modify_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'carbonlist'
        verbose_name = '탄소포인트목록'
    def __str__(self):
        return self.pointtype

class Greenpoint(models.Model):
    pointtype = models.TextField()
    gpoint = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    # modify_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'greenlist'
        verbose_name = '그린포인트목록'
    def __str__(self):
        return self.pointtype

class Carbon(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    point = models.ForeignKey(Carbonpoint, on_delete=models.CASCADE)
    # practice =
    # container =
    # refill =
    # total =
    active = models.BooleanField(default = True)
    quantity = models.PositiveSmallIntegerField(null=True, default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'carbonuser'
        verbose_name = '탄소포인트'

# class Green(models.Model):
#     user =
#     saving =
#     hiking =
#     greenpoint =
#     create_date = models.DateTimeField(auto_now_add=True)
#
# class Vehicle(models.Model):
#     user =
#     stdmileage =
#     confmileage =
#     rdtmileage =
#     rdtrate =
#     create_date = models.DateTimeField(auto_now_add=True)