# Generated by Django 2.2.24 on 2021-11-25 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fruit', models.CharField(max_length=64)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grocessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocessory', models.CharField(max_length=64)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='lentils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lentil', models.CharField(max_length=64)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rice', models.CharField(max_length=64)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vegitables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vegitable', models.CharField(max_length=64)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fruit', to='Market.Fruits')),
                ('Grocessory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Grocessory', to='Market.Grocessory')),
                ('Vegitable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vegitabl', to='Market.Vegitables')),
                ('lentil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lentil', to='Market.lentils')),
                ('rice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ricee', to='Market.Rice')),
            ],
        ),
    ]
