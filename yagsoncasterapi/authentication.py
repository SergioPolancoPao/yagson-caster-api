from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions

class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_X_TOKEN')
        if not token:
            raise exceptions.AuthenticationFailed('Token is required')
        
        if token != settings.SECRET_KEY:
            raise exceptions.AuthenticationFailed('Invalid token')
        