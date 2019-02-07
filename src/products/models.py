from django.db import models
import os
import secrets
import datetime
now = datetime.datetime.now()

# Create your models here.


def get_path(instance, filename):
    _, f_ext = os.path.splitext(filename)
    random_name = secrets.token_hex(8)
    new_filename = random_name+f_ext
    return 'uploads/{}/{}'.format(now.year, new_filename)


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=4, max_digits=20)
    image = models.ImageField(upload_to=get_path)

    def __str__(self):
        return self.title
