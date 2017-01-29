from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=25, default="Rob")
    lastname = models.CharField(max_length=25, default="Cardy")
    email = models.EmailField(default="test@tester.com")
    username = models.CharField(max_length=20, default="cardy31")
    hash = models.CharField(max_length=100, default="cheese")
    age = models.IntegerField(default=30)
    address = models.CharField(max_length=70, default="1 Fake St, Faketown")
    prov = models.CharField(max_length=20, default="ON")
    postal = models.CharField(max_length=7, default="N2B 2W2")
    animalToAdopt = models.CharField(max_length=10, default="Dog")
    adoptWithMedical = models.NullBooleanField(max_length=3,blank=False, null=False, default=False)
    previousOwnership = models.NullBooleanField(max_length=3,blank=False, null=False, default=False)
    owner = models.ForeignKey('auth.User', related_name='member', default=1)


class SwipedAnimal(models.Model):
    animalCode = models.CharField(max_length=50, default="NULL")
    memberUserId = models.IntegerField(default=1)
    owner = models.ForeignKey('auth.User', related_name='swipedanimal', default=1)