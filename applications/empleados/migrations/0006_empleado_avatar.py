# Generated by Django 5.0.7 on 2024-08-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_empleado_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
