# Generated by Django 5.1.7 on 2025-03-27 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_alter_users_managers_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='system.role'),
        ),
    ]
