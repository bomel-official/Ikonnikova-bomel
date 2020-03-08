# Generated by Django 2.1.4 on 2020-03-08 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devs', '0006_auto_20200308_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, default=None, max_length=50, verbose_name='Название (Можно не указывать)')),
                ('file', models.FileField(blank=True, default=None, upload_to='uploads/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.RemoveField(
            model_name='development',
            name='File',
        ),
        migrations.AddField(
            model_name='file',
            name='Development',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='devs.Development'),
        ),
    ]
