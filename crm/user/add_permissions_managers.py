import itertools

from django.apps import apps as global_apps


def create_permissions(apps=global_apps, **kwargs):
    """
    Function called by the app post migration signal to create permissions for
    the managers group
    """
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    group = Group.objects.get(name='managers')
    for codename in [
        '_'.join((f, g)) for f, g in itertools.product(
            ['add', 'change', 'delete', 'view'],
            ['user', 'client', 'contract', 'event']
         )]:
        permission = Permission.objects.get(codename=codename)
        group.permissions.add(permission)
    group.save()