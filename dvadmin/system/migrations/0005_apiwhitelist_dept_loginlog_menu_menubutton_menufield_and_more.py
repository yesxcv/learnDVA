# Generated by Django 5.1.7 on 2025-03-28 02:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_remove_users_user_role_users_role_alter_role_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiWhiteList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('modifier', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改人')),
                ('url', models.CharField(help_text='url地址', max_length=200, verbose_name='url')),
                ('method', models.IntegerField(blank=True, default=0, help_text='接口请求方法', null=True, verbose_name='接口请求方法')),
                ('enable_datasource', models.BooleanField(blank=True, default=True, help_text='激活数据权限', verbose_name='激活数据权限')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '接口白名单',
                'verbose_name_plural': '接口白名单',
                'db_table': 'dvadmin_api_white_list',
                'ordering': ('-create_datetime',),
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('modifier', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改人')),
                ('name', models.CharField(help_text='部门名称', max_length=64, verbose_name='部门名称')),
                ('key', models.CharField(blank=True, help_text='关联字符', max_length=64, null=True, unique=True, verbose_name='关联字符')),
                ('sort', models.IntegerField(default=1, help_text='显示排序', verbose_name='显示排序')),
                ('owner', models.CharField(blank=True, help_text='负责人', max_length=32, null=True, verbose_name='负责人')),
                ('phone', models.CharField(blank=True, help_text='联系电话', max_length=32, null=True, verbose_name='联系电话')),
                ('email', models.EmailField(blank=True, help_text='邮箱', max_length=32, null=True, verbose_name='邮箱')),
                ('status', models.BooleanField(blank=True, default=True, help_text='部门状态', null=True, verbose_name='部门状态')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('parent', models.ForeignKey(blank=True, db_constraint=False, default=None, help_text='上级部门', null=True, on_delete=django.db.models.deletion.CASCADE, to='system.dept', verbose_name='上级部门')),
            ],
            options={
                'verbose_name': '部门表',
                'verbose_name_plural': '部门表',
                'db_table': 'dvadmin_system_dept',
                'ordering': ('sort',),
            },
        ),
        migrations.CreateModel(
            name='LoginLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('modifier', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改人')),
                ('username', models.CharField(blank=True, help_text='登录用户名', max_length=32, null=True, verbose_name='登录用户名')),
                ('ip', models.CharField(blank=True, help_text='登录ip', max_length=32, null=True, verbose_name='登录ip')),
                ('agent', models.TextField(blank=True, help_text='agent信息', null=True, verbose_name='agent信息')),
                ('browser', models.CharField(blank=True, help_text='浏览器名', max_length=200, null=True, verbose_name='浏览器名')),
                ('os', models.CharField(blank=True, help_text='操作系统', max_length=200, null=True, verbose_name='操作系统')),
                ('continent', models.CharField(blank=True, help_text='州', max_length=50, null=True, verbose_name='州')),
                ('country', models.CharField(blank=True, help_text='国家', max_length=50, null=True, verbose_name='国家')),
                ('province', models.CharField(blank=True, help_text='省份', max_length=50, null=True, verbose_name='省份')),
                ('city', models.CharField(blank=True, help_text='城市', max_length=50, null=True, verbose_name='城市')),
                ('district', models.CharField(blank=True, help_text='县区', max_length=50, null=True, verbose_name='县区')),
                ('isp', models.CharField(blank=True, help_text='运营商', max_length=50, null=True, verbose_name='运营商')),
                ('area_code', models.CharField(blank=True, help_text='区域代码', max_length=50, null=True, verbose_name='区域代码')),
                ('country_english', models.CharField(blank=True, help_text='英文全称', max_length=50, null=True, verbose_name='英文全称')),
                ('country_code', models.CharField(blank=True, help_text='简称', max_length=50, null=True, verbose_name='简称')),
                ('longitude', models.CharField(blank=True, help_text='经度', max_length=50, null=True, verbose_name='经度')),
                ('latitude', models.CharField(blank=True, help_text='纬度', max_length=50, null=True, verbose_name='纬度')),
                ('login_type', models.IntegerField(choices=[(1, '普通登录'), (2, '微信扫码登录')], default=1, help_text='登录类型', verbose_name='登录类型')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '登录日志',
                'verbose_name_plural': '登录日志',
                'db_table': 'dvadmin_system_login_log',
                'ordering': ('-create_datetime',),
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('modifier', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改人')),
                ('icon', models.CharField(blank=True, help_text='菜单图标', max_length=64, null=True, verbose_name='菜单图标')),
                ('name', models.CharField(help_text='菜单名称', max_length=64, verbose_name='菜单名称')),
                ('sort', models.IntegerField(blank=True, default=1, help_text='显示排序', null=True, verbose_name='显示排序')),
                ('is_link', models.BooleanField(default=False, help_text='是否外链', verbose_name='是否外链')),
                ('link_url', models.CharField(blank=True, help_text='链接地址', max_length=255, null=True, verbose_name='链接地址')),
                ('is_catalog', models.BooleanField(default=False, help_text='是否目录', verbose_name='是否目录')),
                ('web_path', models.CharField(blank=True, help_text='路由地址', max_length=128, null=True, verbose_name='路由地址')),
                ('component', models.CharField(blank=True, help_text='组件地址', max_length=128, null=True, verbose_name='组件地址')),
                ('component_name', models.CharField(blank=True, help_text='组件名称', max_length=50, null=True, verbose_name='组件名称')),
                ('status', models.BooleanField(blank=True, default=True, help_text='菜单状态', verbose_name='菜单状态')),
                ('cache', models.BooleanField(blank=True, default=False, help_text='是否页面缓存', verbose_name='是否页面缓存')),
                ('visible', models.BooleanField(blank=True, default=True, help_text='侧边栏中是否显示', verbose_name='侧边栏中是否显示')),
                ('is_iframe', models.BooleanField(blank=True, default=False, help_text='框架外显示', verbose_name='框架外显示')),
                ('is_affix', models.BooleanField(blank=True, default=False, help_text='是否固定', verbose_name='是否固定')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('parent', models.ForeignKey(blank=True, db_constraint=False, help_text='上级菜单', null=True, on_delete=django.db.models.deletion.CASCADE, to='system.menu', verbose_name='上级菜单')),
            ],
            options={
                'verbose_name': '菜单表',
                'verbose_name_plural': '菜单表',
                'db_table': 'dvadmin_system_menu',
                'ordering': ('sort',),
            },
        ),
        migrations.CreateModel(
            name='MenuButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('modifier', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改人')),
                ('name', models.CharField(help_text='名称', max_length=64, verbose_name='名称')),
                ('value', models.CharField(help_text='权限值', max_length=64, unique=True, verbose_name='权限值')),
                ('api', models.CharField(help_text='接口地址', max_length=200, verbose_name='接口地址')),
                ('method', models.IntegerField(blank=True, default=0, help_text='接口请求方法', null=True, verbose_name='接口请求方法')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('menu', models.ForeignKey(db_constraint=False, help_text='关联菜单', on_delete=django.db.models.deletion.CASCADE, related_name='menuPermission', to='system.menu', verbose_name='关联菜单')),
            ],
            options={
                'verbose_name': '菜单权限表',
                'verbose_name_plural': '菜单权限表',
                'db_table': 'dvadmin_system_menu_button',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='MenuField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('modifier', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改人')),
                ('model', models.CharField(max_length=64, verbose_name='表名')),
                ('field_name', models.CharField(max_length=64, verbose_name='模型表字段名')),
                ('title', models.CharField(max_length=64, verbose_name='字段显示名')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('menu', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='system.menu', verbose_name='菜单')),
            ],
            options={
                'verbose_name': '菜单字段表',
                'verbose_name_plural': '菜单字段表',
                'db_table': 'dvadmin_system_menu_field',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='FieldPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('modifier', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改人')),
                ('is_query', models.BooleanField(default=1, verbose_name='是否可查询')),
                ('is_create', models.BooleanField(default=1, verbose_name='是否可创建')),
                ('is_update', models.BooleanField(default=1, verbose_name='是否可更新')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('role', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='system.role', verbose_name='角色')),
                ('field', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='menu_field', to='system.menufield', verbose_name='字段')),
            ],
            options={
                'verbose_name': '字段权限表',
                'verbose_name_plural': '字段权限表',
                'db_table': 'dvadmin_system_field_permission',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='RoleMenuButtonPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('modifier', models.CharField(blank=True, max_length=255, null=True, verbose_name='修改人')),
                ('data_range', models.IntegerField(choices=[(0, '仅本人数据权限'), (1, '本部门及以下数据权限'), (2, '本部门数据权限'), (3, '全部数据权限'), (4, '自定数据权限')], default=0, help_text='数据权限范围', verbose_name='数据权限范围')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('dept', models.ManyToManyField(blank=True, db_constraint=False, help_text='数据权限-关联部门', to='system.dept', verbose_name='数据权限-关联部门')),
                ('menu_button', models.ForeignKey(blank=True, db_constraint=False, help_text='关联菜单按钮', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_button_permission', to='system.menubutton', verbose_name='关联菜单按钮')),
                ('role', models.ForeignKey(db_constraint=False, help_text='关联角色', on_delete=django.db.models.deletion.CASCADE, related_name='role_menu_button', to='system.role', verbose_name='关联角色')),
            ],
            options={
                'verbose_name': '角色按钮权限表',
                'verbose_name_plural': '角色按钮权限表',
                'db_table': 'dvadmin_role_menu_button_permission',
                'ordering': ('-create_datetime',),
            },
        ),
    ]
