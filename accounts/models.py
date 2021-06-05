from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=20)
    birthday = models.IntegerField(max_length=20)

    def __str__(self):
        return self.user
