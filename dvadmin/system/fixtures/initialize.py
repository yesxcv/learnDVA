from dvadmin.utils.core_initialize import CoreInitialize
from dvadmin.utils.serializers import CustomModelSerializer
from rest_framework import serializers
from dvadmin.system.fixtures.initSerializer import (
    UsersInitSerializer,
    DeptInitSerializer,
    RoleInitSerializer,
    MenuInitSerializer,
    ApiWhiteListInitSerializer,
    DictionaryInitSerializer,
    SystemConfigInitSerializer,
    RoleMenuInitSerializer,
    RoleMenuButtonInitSerializer,
)


class Initialize(CoreInitialize):
    def init_role(self):
        """
        初始化角色信息
        """
        self.init_base(RoleInitSerializer, unique_fields=["key"])

