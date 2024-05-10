# Generated by Django 5.0.6 on 2024-05-10 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notes.category'),
        ),
    ]