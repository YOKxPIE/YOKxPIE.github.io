# Generated by Django 3.2.6 on 2021-09-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(blank=True, related_name='students', to='courses.Course'),
        ),
        migrations.DeleteModel(
            name='Take',
        ),
    ]
