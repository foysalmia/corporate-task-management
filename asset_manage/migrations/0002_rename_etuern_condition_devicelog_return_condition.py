# Generated by Django 5.0.2 on 2024-02-07 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset_manage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devicelog',
            old_name='etuern_condition',
            new_name='return_condition',
        ),
    ]