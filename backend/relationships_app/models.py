from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Admin(models.Model):
    user = models.ForeignKey(User, related_name='admin_list', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=64)
    start_date = models.DateTimeField()

    def __str__(self):
        return f'{self.full_name}'

class Corporation(models.Model):
    name = models.CharField(max_length=64)
    founded_on = models.DateField()
    type = models.CharField(max_length=16)
    country = models.CharField(max_length=32)
    admin = models.OneToOneField(Admin, related_name='corporation', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Manager(models.Model):
    user = models.ForeignKey(User, related_name='managers', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    corporation = models.OneToOneField(Corporation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.full_name}'
