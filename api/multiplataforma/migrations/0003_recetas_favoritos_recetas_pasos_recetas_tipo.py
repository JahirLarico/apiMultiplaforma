# Generated by Django 4.1.3 on 2022-11-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplataforma', '0002_alter_recetas_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='recetas',
            name='favoritos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recetas',
            name='pasos',
            field=models.CharField(default='Aqui iran los pasos de la receta', max_length=500),
        ),
        migrations.AddField(
            model_name='recetas',
            name='tipo',
            field=models.CharField(default='tipo de comida', max_length=100),
        ),
    ]
