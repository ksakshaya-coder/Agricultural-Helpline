# Generated by Django 3.1.3 on 2020-11-19 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_weather_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ask_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.IntegerField()),
                ('question', models.TextField(max_length=3000, verbose_name='Question')),
                ('answer', models.TextField(max_length=3000, verbose_name='Answer')),
                ('expert_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.register_detail')),
            ],
        ),
    ]