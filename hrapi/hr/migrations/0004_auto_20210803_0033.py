# Generated by Django 3.2.5 on 2021-08-03 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='industry',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='years_of_experience',
            field=models.IntegerField(null=True),
        ),
    ]
