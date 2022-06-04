from django.db import models
from django.conf import settings
from client.models import Client


class Contract(models.Model):
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    client = models.ForeignKey(
        to=Client, on_delete=models.SET_NULL, null=True)
    project_name = models.CharField(max_length=100)
    signed = models.BooleanField(default=False)
    amount = models.FloatField(null=True)
    payment_due_date = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    def __str__(self):
        return f"Contrat: {self.project_name}"
