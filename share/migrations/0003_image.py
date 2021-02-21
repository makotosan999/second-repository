# Generated by Django 3.0.4 on 2020-12-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
