from dvadmin.utils.json_response import SuccessResponse
from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin.system.models import Role
from dvadmin.utils.serializers import CustomModelSerializer
from rest_framework import serializers



class RoleSerializer(CustomModelSerializer):
    """
    角色-序列化器
    """
    users = serializers.SerializerMethodField()

    @staticmethod
    def get_users(instance):
        users = instance.users_set.exclude(id=1).values('id', 'name', 'dept__name')
        return users

    class Meta:
        model = Role
        fields = "__all__"
        read_only_fields = ["id"]





class RoleViewSet(CustomModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    def get_all_roles(self,request):
        roles = request.user.role.filter(status=True)
        return  SuccessResponse(data=RoleSerializer(roles,many=True).data)