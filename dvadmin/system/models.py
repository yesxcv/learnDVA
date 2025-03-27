from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from dvadmin.utils.models import CoreModel,table_prefix

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
    class Meta:
        db_table = table_prefix + "system_users"
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name
        ordering = ("-create_datetime",)
    def __str__(self):
        return  self.username
