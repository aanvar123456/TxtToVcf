# Generated by Django 3.2.13 on 2022-10-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToVcf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='txtfile',
            name='vcf',
            field=models.FileField(default=11, upload_to='Files'),
            preserve_default=False,
        ),
    ]