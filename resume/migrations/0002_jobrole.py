# Generated by Django 4.1 on 2023-09-16 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_roles', to='resume.resume')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
