# Generated by Django 4.0.4 on 2022-05-11 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_image_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['img_id']},
        ),
    ]
