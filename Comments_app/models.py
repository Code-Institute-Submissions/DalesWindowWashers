# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from DalesWindowWashers import settings

class Post(models.Model):

    class Meta:
        app_label = "Comments_app"

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = HTMLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content


