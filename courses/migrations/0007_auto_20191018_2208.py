# Generated by Django 2.2.2 on 2019-10-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='topic',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]