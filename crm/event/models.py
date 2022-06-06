from django.db import models
from contract.models import Contract
from django.conf import settings


class Event(models.Model):
    """  Event model    """
    contract = models.OneToOneField(
        to=Contract,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='event')
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    attendees = models.IntegerField(null=True)
    event_date = models.DateField(null=True)
    notes = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    def __str__(self):
        return f"Evènement: {self.contract.project_name}"