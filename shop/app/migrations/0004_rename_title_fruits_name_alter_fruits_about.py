# Generated by Django 4.1.6 on 2023-03-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fruits',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='fruits',
            name='about',
            field=models.TextField(),
        ),
    ]