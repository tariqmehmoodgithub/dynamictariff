# Generated by Django 3.1.1 on 2020-11-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201116_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbluser',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
