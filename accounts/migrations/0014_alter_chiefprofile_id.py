# Generated by Django 4.1 on 2022-09-30 09:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_chiefprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('54779a58-d446-4376-806c-25d2b3115cf7'), editable=False, primary_key=True, serialize=False),
        ),
    ]
