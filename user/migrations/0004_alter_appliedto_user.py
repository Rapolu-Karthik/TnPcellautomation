# Generated by Django 3.2.7 on 2021-11-29 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20211129_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedto',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
