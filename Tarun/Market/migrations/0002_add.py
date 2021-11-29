# Generated by Django 2.2.24 on 2021-11-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fruits', models.CharField(max_length=64)),
                ('Price', models.IntegerField()),
                ('fruits', models.ManyToManyField(blank=True, related_name='addfruits', to='Market.User')),
            ],
        ),
    ]