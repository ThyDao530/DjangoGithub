# Generated by Django 2.0.4 on 2018-04-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20180419_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default='studentsAvatar/None/no-img.jpg', upload_to='studentsAvatar/'),
        ),
    ]