# Generated by Django 3.0.2 on 2020-02-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20200223_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='priority',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='goal',
            name='success_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=12, null=True),
        ),
    ]