# Generated by Django 3.2.18 on 2023-05-12 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('murage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
