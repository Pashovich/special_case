from django.db import models


class FormModel(models.Model):
    id = models.AutoField(primary_key = True)
    email = models.CharField(max_length = 100, null = False, default = '', unique = True)
    name = models.CharField(max_length = 100, default = '', null = False)
