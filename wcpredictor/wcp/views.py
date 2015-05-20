from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from wcpredictor.wcp.serializers import UserProfileSerializer
from wcpredictor.wcp import models


class BaseAuthView(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)


class UserProfileViewSet(BaseAuthView):

    queryset = models.UserProfile.objects.all()
    serializer_class = UserProfileSerializer
