from django.conf.urls import url
from .views_api import (authenticate_user, change_password, personal_info, user)

urlpatterns = [
    url(r'authenticate/', authenticate_user),
    url(r'change-password/', change_password),
    url(r'personal-info/', personal_info),
    url(r'', user)
]
