# -*- coding: utf-8 -*-

from django.db import models


class Nomination(models.Model):

    name = models.CharField("Название", max_length=1000)
    description = models.CharField("Описание", max_length=5000)

class Application(models.Model):

    name = models.CharField("Название", max_length=1000)
    description = models.CharField("Описание", max_length=5000)

    work = models.FileField("Работа", upload_to='works')

    nomination = models.ForeignKey(Nomination, null=False, blank=False)
