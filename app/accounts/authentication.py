import pytz
from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class ExpiringTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key, request=None):
        models = self.get_model()
        try:
            token = models.objects.select_related("user").get(key=key)
        except models.DoesNotExist:
            raise AuthenticationFailed(
                {"error": "Invalid or Inactive Token", "is_authenticated": False}
            )

        if not token.user.is_active:
            raise AuthenticationFailed(
                {"error": "Invalid user", "is_authenticated": False}
            )

        utc_now = timezone.now()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        if token.created < utc_now - settings.AUTH_TOKEN_VALIDITY:
            token.delete()
            raise AuthenticationFailed(
                {"error": "Token has expired", "is_authenticated": "No"}
            )
        else:
            token.created = utc_now
            token.save()
            
        return token.user, token