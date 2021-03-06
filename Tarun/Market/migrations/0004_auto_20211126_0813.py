# Generated by Django 2.2.24 on 2021-11-26 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0003_auto_20211126_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFruits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fruit', to='Market.Fruits')),
                ('Grocessory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Grocessory', to='Market.Grocessory')),
                ('Vegitable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vegitabl', to='Market.Vegitables')),
                ('lentil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lentil', to='Market.lentils')),
                ('rice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ricee', to='Market.Rice')),
            ],
        ),
        migrations.AlterField(
            model_name='add',
            name='fruits',
            field=models.ManyToManyField(blank=True, related_name='addfruits', to='Market.UserFruits'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
