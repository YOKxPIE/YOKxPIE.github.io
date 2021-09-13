# Generated by Django 3.2.7 on 2021-09-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100, null=True)),
                ('Last_name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('student_id', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='c_name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]