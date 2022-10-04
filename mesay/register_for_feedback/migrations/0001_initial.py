# Generated by Django 4.1.1 on 2022-10-04 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=100)),
                ('Lname', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('PhoneNo', models.IntegerField()),
                ('Feedback', models.TextField()),
                ('Img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
