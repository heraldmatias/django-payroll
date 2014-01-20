__author__ = 'holivares'
from inei.auth.models import Usuario


class EndesBackend(object):
    """
    Authenticates against django.contrib.auth.models.User.
    """
    supports_inactive_user = True

    # TODO: Model, login attribute name and password attribute name should be
    # configurable.
    def authenticate(self, username=None, password=None):
        if username and password:
            try:
                user = Usuario.objects.get(username=username)
                user.check_password(password)
            except Usuario.DoesNotExist:
                # Create a new user. Note that we can set password
                # to anything, because it won't be checked; the password
                # from settings.py will.
                user = Usuario(username=username, password=password)
                user.is_admin = False
                user.save()
            return user
        return None

    def get_group_permissions(self, user_obj, obj=None):
        """
        Returns a set of permission strings that this user has through his/her
        groups.
        """
        return set()

    def get_all_permissions(self, user_obj, obj=None):
        return set()

    def has_perm(self, user_obj, perm, obj=None):
        if not user_obj.is_active:
            return False
        return perm in self.get_all_permissions(user_obj, obj)

    def has_module_perms(self, user_obj, app_label):
        """
        Returns True if user_obj has any permissions in the given app_label.
        """
        if not user_obj.is_active:
            return False
        for perm in self.get_all_permissions(user_obj):
            if perm[:perm.index('.')] == app_label:
                return True
        return False

    def get_user(self, user_id):
        try:
            user = Usuario.objects.get(pk=user_id)
            return user
        except Usuario.DoesNotExist:
            return None