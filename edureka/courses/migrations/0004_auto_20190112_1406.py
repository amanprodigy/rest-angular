# Generated by Django 2.1.4 on 2019-01-12 14:06

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190112_1311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order'], 'verbose_name': 'content', 'verbose_name_plural': 'contents'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order'], 'verbose_name': 'module', 'verbose_name_plural': 'modules'},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
