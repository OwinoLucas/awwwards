# Generated by Django 2.2.6 on 2020-06-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myawards', '0005_auto_20200606_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='technologies',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]