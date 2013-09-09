# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

class ListSubscriptions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    list_id = models.IntegerField(null=True, blank=True)
    timestamp = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'list_subscriptions'

class Lists(models.Model):
    id = models.IntegerField(primary_key=True)
    list_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100L, blank=True)
    description = models.CharField(max_length=200L, blank=True)
    owner_twitter_id = models.IntegerField(null=True, blank=True)
    timestamp = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'lists'

class PocketLogs(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    status_id = models.IntegerField()
    timestamp = models.IntegerField()
    class Meta:
        db_table = 'pocket_logs'

class StatusMessages(models.Model):
    id = models.IntegerField(primary_key=True)
    list_id = models.IntegerField(null=True, blank=True)
    url = models.IntegerField(null=True, blank=True)
    retweets = models.IntegerField(null=True, blank=True)
    favorites = models.IntegerField(null=True, blank=True)
    owner_followers = models.IntegerField(null=True, blank=True)
    timestamp = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'status_messages'

class TwythonDjangoOauthTwitterprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, unique=True)
    oauth_token = models.CharField(max_length=200L)
    oauth_secret = models.CharField(max_length=200L)
    class Meta:
        db_table = 'twython_django_oauth_twitterprofile'

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    twitter_id = models.IntegerField()
    pocket_token = models.CharField(max_length=200L, blank=True)
    twitter_token = models.CharField(max_length=200L)
    twitter_handle = models.CharField(max_length=100L, blank=True)
    email = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'users'

