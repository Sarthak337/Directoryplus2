# Generated by Django 3.0.5 on 2020-05-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directoryplus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics1')),
                ('food_name', models.CharField(max_length=100)),
            ],
        ),
    ]
