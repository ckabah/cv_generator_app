import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class PasswordTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
    
account_token_generation = PasswordTokenGenerator()

UserModel = get_user_model()
class EmailBackend(ModelBackend):
    def authenticate(self, request, user_name=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(user_name__iexact=user_name) | Q(email__iexact=user_name))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(username__iexact=user_name) | Q(email__iexact=user_name)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user