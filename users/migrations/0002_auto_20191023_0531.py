# Generated by Django 2.2.2 on 2019-10-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanager',
            name='prev_result',
            field=models.CharField(choices=[('easy', 'Lower-Credit'), ('difficult', 'Upper-Credit'), ('easy', 'Pass'), ('difficult', 'Distinction')], max_length=20, null=True),
        ),
    ]
