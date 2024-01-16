from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField, TextField, Model


class ResizedImageField:
    pass



class Trener(Model):
    fist_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    job = CharField(max_length=255),
    text = TextField()



