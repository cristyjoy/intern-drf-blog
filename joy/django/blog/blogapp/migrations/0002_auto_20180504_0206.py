# Generated by Django 2.0.5 on 2018-05-04 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft'), ('hidden', 'Hidden'), ('archived', 'Archived')], default='draft', max_length=10),
        ),
    ]
