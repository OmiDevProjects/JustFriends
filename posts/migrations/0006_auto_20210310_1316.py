# Generated by Django 3.0.8 on 2021-03-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='action',
            field=models.CharField(choices=[('NO_FILTER', 'no filter'), ('COLORIZED', 'colorized'), ('GRAYSCALE', 'grayscale'), ('BLURRED', 'blurred'), ('BINARY', 'binary'), ('INVERT', 'invert')], default='NO_FILTER', max_length=50, null=True),
        ),
    ]
