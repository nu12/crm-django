# Generated by Django 3.1.5 on 2021-01-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='phoned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lead',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='lead',
            name='source',
            field=models.CharField(blank=True, choices=[('Youtube', 'Youtube'), ('Google', 'Google'), ('Newsletter', 'Newsletter')], max_length=100),
        ),
        migrations.AddField(
            model_name='lead',
            name='special_files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
