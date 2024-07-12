# Generated by Django 5.0.6 on 2024-07-10 16:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0004_alter_add_job_comapany_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='add_job',
            options={'ordering': ['salary']},
        ),
        migrations.AddField(
            model_name='add_job',
            name='job_category',
            field=models.ManyToManyField(to='buyer.category'),
        ),
        migrations.CreateModel(
            name='Reveiw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('☆☆☆☆⭐', '☆☆☆☆⭐'), ('☆☆☆⭐⭐', '☆☆☆⭐⭐'), ('☆☆⭐⭐⭐', '☆☆⭐⭐⭐'), ('☆⭐⭐⭐⭐', '☆⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=10)),
                ('reveiw_text', models.TextField()),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.add_job')),
            ],
        ),
    ]
