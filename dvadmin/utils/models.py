from django.db import models

class CoreModel(models.Model):
    """
    核心标准模型(所有模型继承此模型)
    """
    create_datetime = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_datetime = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    creator = models.ForeignKey(
        "system.Users",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="创建人",
        db_constraint=False
    )
    modifier = models.CharField(max_length=255,null=True,blank=True,verbose_name="修改人")
    class Meta:
        abstract = True
        verbose_name = "核心模型"
        verbose_name_plural = verbose_name
table_prefix = "dvadmin_"
