# Generated by Django 4.1 on 2022-09-27 14:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_chiefprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiefprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1c1220a1-403f-48b2-8c49-f4ec63f7e54a'), editable=False, primary_key=True, serialize=False),
        ),
    ]