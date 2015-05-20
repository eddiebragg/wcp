from rest_framework import serializers
from wcpredictor.wcp import models
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    user = UserSerializer()

    class Meta:
        model = models.UserProfile
        fields = ('firstname', 'surname', 'user')
