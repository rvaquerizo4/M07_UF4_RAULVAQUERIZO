# Generated by Django 4.1.6 on 2023-04-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institut', '0005_remove_alum_edad_remove_prof_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alum',
            name='poblacion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='prof',
            name='poblacion',
            field=models.CharField(max_length=50),
        ),
    ]
