# Generated by Django 2.1.5 on 2019-01-09 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Railwayticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='status',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]