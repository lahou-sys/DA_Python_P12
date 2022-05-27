from django.db import models
from django.contrib.auth.models import User

from client.models import Client
from event.models import Event


class Support(models.Model):
    """  Support model    """
    user = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)


class EventSupport(models.Model):
    """  EventSupport model    """
    user = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)
    event = models.ForeignKey(
        Event,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)
    client = models.ForeignKey(
        Client,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)


class Sales(models.Model):
    """  Sales model    """
    user = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)


class SalesClient(models.Model):
    """  SalesClient model    """
    user = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)
    client = models.ForeignKey(
        Client,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)

