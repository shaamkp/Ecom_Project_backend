# Generated by Django 4.1 on 2022-10-04 07:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_chiefprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7d1ca83b-b095-404f-8d90-80671fb3ba6b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
