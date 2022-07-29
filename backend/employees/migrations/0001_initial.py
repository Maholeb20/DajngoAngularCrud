# Generated by Django 4.0.5 on 2022-06-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('deptname', models.CharField(blank=True, max_length=25, null=True)),
                ('location', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=25, unique=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('sal', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
    ]
