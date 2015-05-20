
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username


class Team(models.Model):
    name = models.CharField(max_length=100)


class Tournament(models.Model):
    nams = models.CharField(max_length=100)


class Group(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team)


class Game(models.Model):
    team_one = models.ForeignKey(Team, related_name="game_team_one")
    team_two = models.ForeignKey(Team, related_name="game_team_two")
    game_time = models.DateTimeField()
    group = models.ForeignKey(Group)
