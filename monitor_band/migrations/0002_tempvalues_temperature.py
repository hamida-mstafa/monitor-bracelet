# Generated by Django 2.1.7 on 2019-02-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_band', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempvalues',
            name='temperature',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]