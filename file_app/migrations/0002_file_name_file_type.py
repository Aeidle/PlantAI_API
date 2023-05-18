# Generated by Django 4.2 on 2023-05-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='file',
            name='type',
            field=models.CharField(choices=[('fruit', 'Fruit'), ('leaf', 'Leaf')], default='fruit', max_length=5),
        ),
    ]