from django.db import models
from importlib import import_module
from application import settings
from django.apps import apps
from django.conf import settings

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


def get_model_from_app(app_name):
    """获取模型里的字段"""
    model_module = import_module(app_name + ".models")
    exclude_models = getattr(model_module, "exclude_models", [])
    filter_model = [
        value
        for key, value in model_module.__dict__.items()
        if key != "CoreModel"
        and isinstance(value, type)
        and issubclass(value, models.Model)
        and key not in exclude_models
    ]
    model_list = []
    for model in filter_model:
        if model.__name__ == "AbstractUser":
            continue
        fields = [
            {"title": field.verbose_name, "name": field.name, "object": field}
            for field in model._meta.fields
        ]
        model_list.append(
            {
                "app": app_name,
                "verbose": model._meta.verbose_name,
                "model": model.__name__,
                "object": model,
                "fields": fields,
            }
        )
    return model_list


def get_custom_app_models(app_name=None):
    """
    获取所有项目下的app里的models
    """
    if app_name:
        return get_model_from_app(app_name)
    all_apps = apps.get_app_configs()
    res = []
    for app in all_apps:
        if app.name.startswith('django'):
            continue
        if app.name in settings.COLUMN_EXCLUDE_APPS:
            continue
        try:
            all_models = get_model_from_app(app.name)
            if all_models:
                for model in all_models:
                    res.append(model)
        except Exception as e:
            pass
    return res