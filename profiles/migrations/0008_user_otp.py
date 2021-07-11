# Generated by Django 3.0.8 on 2021-03-25 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_remove_profile_is_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('otp', models.SmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
    ]