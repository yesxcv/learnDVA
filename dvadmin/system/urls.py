from dvadmin.system.views.message_center import MessageCenterViewSet
from rest_framework import routers
from django.urls import path

system_url = routers.SimpleRouter()

system_url.register('message',MessageCenterViewSet)

urlpatterns = system_url.urls

