from django.http import HttpResponse

from dvadmin.utils.viewset import CustomModelViewSet
from django.db.models import F
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from dvadmin.system.models import RoleMenuPermission, Menu, MenuButton
from dvadmin.utils.json_response import DetailResponse, ErrorResponse
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet

class RoleMenuPermissionViewSet(CustomModelViewSet):
    @action(methods=['post'], detail=False)
    def save_auth(self, request):
        # 处理角色-菜单权限的批量更新
        role_id = request.data.get('role')
        new_menu_ids = set(request.data.get('menu', []))

        # 获取现有权限
        current_menu_ids = set(RoleMenuPermission.objects.filter(role_id=role_id)
                               .values_list('menu_id', flat=True))

        # 计算需要添加和删除的权限
        add_ids = new_menu_ids - current_menu_ids
        del_ids = current_menu_ids - new_menu_ids

        # 批量操作
        RoleMenuPermission.objects.bulk_create([
            RoleMenuPermission(role_id=role_id, menu_id=menu_id)
            for menu_id in add_ids
        ])
        RoleMenuPermission.objects.filter(role_id=role_id, menu_id__in=del_ids).delete()

        return HttpResponse(msg="权限更新成功")
