from yaml import serialize

from dvadmin.system.models import Users
from dvadmin.system.views.role import RoleSerializer
from dvadmin.utils.serializers import CustomModelSerializer
from rest_framework import serializers
from django_restql.fields import DynamicSerializerMethodField



class UserSerializer(CustomModelSerializer):
    # dept_name = serializers.CharField(source=dept,name)
    role_info = DynamicSerializerMethodField()
    class Meta:
        model = Users
        read_only_fields = ['id']
        exclude = ['password']
    def get_role_info(self,instance,parsed_query):
        roles = instance.role.all()
        serializer = RoleSerializer(
            roles,many=True,parsed_query=parsed_query
        )
        return serializer.data