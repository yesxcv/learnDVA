import hashlib
from idlelib.iomenu import encoding

from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

from application import settings
from dvadmin.utils.models import CoreModel,table_prefix
import hashlib

class Role(CoreModel):
    name = models.CharField(max_length=64, verbose_name="角色名称", help_text="角色名称")
    key = models.CharField(max_length=64, unique=True, verbose_name="权限字符", help_text="权限字符")
    sort = models.IntegerField(default=1, verbose_name="角色顺序", help_text="角色顺序")
    status = models.BooleanField(default=True, verbose_name="角色状态", help_text="角色状态")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='创建者',
        related_name='created_roles'  # 添加这个
)
    class Meta:
        db_table = table_prefix + "system_role"
        verbose_name = "角色表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)

class CustomUserManager(UserManager):
    """
    重写create_superuser方法实现:
    1.MD5密码加密
    2.自动绑定管理员角色
    3.异常处理机制
    """
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        user = super().create_superuser(username,email,password,**extra_fields)
        user.set_password(password)
        try:
            admin_role = Role.objects.get(name="管理员")
            user.role.add(admin_role)
            user.save(using=self._db)
            return user
        except ObjectDoesNotExist:
            user.delete()
            raise  ValidationError("管理员角色不存在")




class Users(CoreModel,AbstractUser):
    #继承AbstractUser已有字段：username, password, email, first_name, last_name, etc.
    mobile = models.CharField(max_length=20,verbose_name="手机号",blank=True)
    avatar = models.CharField(max_length=256,verbose_name="头像",blank=True)
    GENDER_CHOICES = (
        (0,"未知"),
        ("1","男"),
        ("2","女")
    )
    gender = models.SmallIntegerField(
        choices = GENDER_CHOICES,
        default=0,
        verbose_name="性别"
    )
    objects = CustomUserManager()
    role = models.ManyToManyField(to="Role", blank=True, verbose_name="关联角色", db_constraint=False,
                                  help_text="关联角色")

    def set_password(self, raw_password):
        super().set_password(hashlib.md5(raw_password.encode(encoding="UTF-8")).hexdigest())

    class Meta:
        db_table = table_prefix + "system_users"
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name
        ordering = ("-create_datetime",)
    def __str__(self):
        return  self.username
