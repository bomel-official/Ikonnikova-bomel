# Generated by Django 2.1.4 on 2020-03-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20200309_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardcategory',
            name='Title',
            field=models.CharField(max_length=50, verbose_name='Название категории'),
        ),
    ]
