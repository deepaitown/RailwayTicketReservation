# Generated by Django 2.1.5 on 2019-01-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Railwayticket', '0003_auto_20190109_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
