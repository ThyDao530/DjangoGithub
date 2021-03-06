# Generated by Django 2.0.4 on 2018-04-15 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name ', max_length=200)),
                ('avatar', models.ImageField(default='avatar/None/no-img.jpg', upload_to='studentsAvatar/')),
                ('studentID', models.CharField(help_text='Enter student ID', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name ', max_length=200)),
                ('subjectID', models.CharField(help_text='Enter subject ID', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='studentID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Student'),
        ),
        migrations.AddField(
            model_name='score',
            name='subjID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Subject'),
        ),
    ]
