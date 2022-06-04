from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Default user for crm """

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
