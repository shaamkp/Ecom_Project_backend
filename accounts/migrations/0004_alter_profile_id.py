# Generated by Django 4.1 on 2022-09-27 06:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4bd92827-34b8-4bdb-a7b2-a3fda4fffffe'), editable=False, primary_key=True, serialize=False),
        ),
    ]
