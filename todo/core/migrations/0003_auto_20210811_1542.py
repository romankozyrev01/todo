# Generated by Django 3.2.6 on 2021-08-11 15:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_dayset_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayset',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterUniqueTogether(
            name='dayset',
            unique_together={('date', 'user')},
        ),
    ]
