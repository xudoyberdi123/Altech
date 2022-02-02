from django.db import models


# Create your models here.

def default_log():
    return {'state': 0}


class Log(models.Model):
    user_id = models.BigIntegerField(primary_key=True, null=False)
    messages = models.JSONField(blank=True, null=True, default=default_log())

    def __str__(self):
        return "#%s" % self.user_id


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True, null=False)
    menu_log = models.IntegerField(null=True)
