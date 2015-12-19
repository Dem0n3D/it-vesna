# -*- coding: UTF-8 -*-

from django.db import models


class Menu(models.Model):

    name = models.CharField("Название", max_length=1000)

    node = models.ForeignKey("Node")

    def __str__(self):
        return self.name


class Node(models.Model):

    title = models.CharField("Пункт", max_length=1000)
    url = models.CharField("URL", max_length=1000, blank=True)

    order = models.IntegerField("Порядковый №", null=True, blank=True, default=0)

    parent = models.ForeignKey("Node", related_name="childrens", null=True, blank=True)

    def __str__(self):
        return self.title
