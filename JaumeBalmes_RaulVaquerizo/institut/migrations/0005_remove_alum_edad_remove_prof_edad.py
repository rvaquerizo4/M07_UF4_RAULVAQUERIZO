# Generated by Django 4.1.6 on 2023-04-20 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institut', '0004_alter_alum_clase_alter_prof_clase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alum',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='prof',
            name='edad',
        ),
    ]