# Generated by Django 3.0.5 on 2020-06-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200603_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='img.png', null=True, upload_to=''),
        ),
    ]
