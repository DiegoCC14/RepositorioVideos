# Generated by Django 4.1.4 on 2022-12-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_db', '0003_alter_video_id_estado_alter_video_id_origen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='fecha_ingreso',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
