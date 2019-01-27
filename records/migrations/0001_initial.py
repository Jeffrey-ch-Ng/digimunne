# Generated by Django 2.1.5 on 2019-01-27 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('year_ob', models.CharField(max_length=4)),
                ('month_ob', models.CharField(max_length=2)),
                ('day_ob', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('month', models.CharField(max_length=2)),
                ('day', models.CharField(max_length=2)),
                ('disease_name', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Patient')),
            ],
            options={
                'ordering': ('disease_name',),
            },
        ),
    ]