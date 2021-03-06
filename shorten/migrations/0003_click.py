# Generated by Django 2.1 on 2018-08-14 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0002_auto_20180814_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('referer', models.URLField(blank=True, null=True)),
                ('short_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clicks', to='shorten.ShortURL')),
            ],
        ),
    ]
