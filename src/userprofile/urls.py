# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
from django.conf.urls import url,include
from .views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from profiles import views as profile_views


urlpatterns = [
    url(r'^$', home, name='home'),  
	url(r'^about/$', profile_views.about , name='about'),
    url(r'^profile/$', userProfile, name='profile'),
    url(r'^profile/edit/$', edit_profile, name='edit_profile'),
]
