# Generated by Django 2.2.2 on 2019-10-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20191018_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.TextField(blank=True, default='Youtube Video embedd code', max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='video',
            field=models.TextField(blank=True, default='Youtube Video embedd code', max_length=900, null=True),
        ),
    ]