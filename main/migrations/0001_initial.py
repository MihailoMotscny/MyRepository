# Generated by Django 4.2.2 on 2023-06-30 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=0, upload_to='images/')),
                ('idcheckimg', models.CharField(blank=True, max_length=230, verbose_name='ID:')),
            ],
        ),
    ]