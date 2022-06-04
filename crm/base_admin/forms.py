from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.forms import AdminAuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class BaseAdminAuthenticationForm(AdminAuthenticationForm):
    """
    Custom authentication form that allows users from the group "managers
    to log in to the basic admin site.
    """
    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': _(
            "Please enter the correct %(username)s and password for a "
            "management group account or superuser. Note that both fields may "
            "be case-sensitive."
        ),
    }

    def confirm_login_allowed(self, user):
        if ("managers" not in (group.name for group in user.groups.all())) and not user.is_staff:
            raise ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )
        if not user.is_active:
            raise ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )
