# Generated by Django 2.1.5 on 2019-02-08 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default='2019-01-02 05:22', verbose_name='date published'),
            preserve_default=False,
        ),
    ]
