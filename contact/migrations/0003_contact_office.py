# Generated by Django 4.2.2 on 2023-06-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='office',
            field=models.CharField(choices=[('administrativo', 'administrativo'), ('estagiario', 'estagiario'), ('defensor', 'defensor')], default=1, max_length=14),
            preserve_default=False,
        ),
    ]
