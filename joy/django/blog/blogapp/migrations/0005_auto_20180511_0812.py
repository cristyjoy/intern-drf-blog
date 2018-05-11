# Generated by Django 2.0.5 on 2018-05-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20180507_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft'), ('archived', 'Archived')], default='draft', max_length=10),
        ),
    ]
