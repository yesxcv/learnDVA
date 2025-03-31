from dvadmin.system.models import Users
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