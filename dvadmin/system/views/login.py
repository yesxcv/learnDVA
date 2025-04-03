from typing import Any

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from dvadmin.system.models import Users


class LoginTokenSerializer(TokenObtainPairSerializer):
    """
    login serializer
    """

    class Meta:
        model = Users
        fields = "__all__"
        read_only_fields = ["id"]

    default_error_messages = {"no_active_account":"账号/密码不正确"}

    def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
        data = super().validate(attrs)
        # data["name"] = self.name
        data['userid'] = self.user.id
        return {"code": 2000, "msg": "请求成功", 'data': data}


class LoginTokenView(TokenObtainPairView):
    serializer_class = LoginTokenSerializer
    permission_classes = []
