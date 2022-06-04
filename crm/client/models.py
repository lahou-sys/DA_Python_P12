from django.db import models
from django.conf import settings


class Client(models.Model):
    """ Clients model    """
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=250)
    converted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.company_name}"