# Generated by Django 4.1.3 on 2022-12-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teacher_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
