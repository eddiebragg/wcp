
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils.models import TimeStampedModel
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(User, related_name="profile")
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __unicode__(self):
        return u'Profile of user: {}'.format(self.user.username)


class Team(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Tournament(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Group(TimeStampedModel):
    name = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament, related_name="tournament_groups")

    def __unicode__(self):
        return u'{} - {}'.format(self.tournament, self.name)


class GroupTeam(TimeStampedModel):
    group = models.ForeignKey(Group, related_name="group_teams")
    team = models.ForeignKey(Team, related_name="groups")


class Game(TimeStampedModel):
    team_one = models.ForeignKey(Team, related_name="game_team_one")
    team_two = models.ForeignKey(Team, related_name="game_team_two")
    game_time = models.DateTimeField()
    group = models.ForeignKey(Group)
    team_one_score = models.IntegerField(default=0)
    team_two_score = models.IntegerField(default=0)
