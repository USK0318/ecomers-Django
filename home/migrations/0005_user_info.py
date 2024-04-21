# Generated by Django 4.2.6 on 2024-04-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_mobile', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='profile_pics')),
            ],
        ),
    ]
