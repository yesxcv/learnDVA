from dvadmin.system.views.message_center import MessageCenterViewSet
from rest_framework import routers
from django.urls import path
from dvadmin.system.views.login import LoginTokenView

system_url = routers.SimpleRouter()

system_url.register('message',MessageCenterViewSet)

urlpatterns = [
    path("token",LoginTokenView.as_view())
]


urlpatterns += system_url.urls

