# Generated by Django 2.1.5 on 2019-01-27 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccination',
            name='patient',
        ),
        migrations.AddField(
            model_name='patient',
            name='vaccinations',
            field=models.ManyToManyField(to='records.Vaccination'),
        ),
        migrations.AddField(
            model_name='vaccination',
            name='expiration_date',
            field=models.CharField(default=2003, max_length=200),
            preserve_default=False,
        ),
    ]
