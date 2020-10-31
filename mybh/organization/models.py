from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=300)
    adress = models.CharField(max_length=500)
    inn = models.CharField(max_length=50)
    kpp = models.CharField(max_length=50)
    director = models.ForeignKey('organization.Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GroupRights(models.Model):
    rights = models.CharField(max_length=200)


class Employee(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    groupRights = models.ForeignKey(GroupRights, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employment(models.Model):
    workman = models.ForeignKey(Employee, on_delete=models.CASCADE)
    corporation = models.ForeignKey(Organization, on_delete=models.CASCADE)
