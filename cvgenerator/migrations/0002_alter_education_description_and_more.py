# Generated by Django 4.1.2 on 2022-10-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvgenerator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='education',
            name='etablisement',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='education',
            name='level',
            field=models.CharField(blank=True, max_length=20, verbose_name='Niveau de formation'),
        ),
        migrations.AlterField(
            model_name='profexperience',
            name='company',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='detail',
            field=models.TextField(max_length=2000),
        ),
    ]