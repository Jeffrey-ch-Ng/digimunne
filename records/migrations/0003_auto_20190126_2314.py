# Generated by Django 2.1.5 on 2019-01-27 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20190126_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='day_ob',
            new_name='day_of_birth',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='month_ob',
            new_name='month_of_birth',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='year_ob',
            new_name='year_of_birth',
        ),
    ]
