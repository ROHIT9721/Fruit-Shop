# Generated by Django 4.1.6 on 2023-03-03 12:39

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_title_fruits_name_alter_fruits_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruits',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]
