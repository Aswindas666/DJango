# Generated by Django 4.1.3 on 2022-12-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=255)),
                ('decpt', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
