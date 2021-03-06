# Generated by Django 3.0.6 on 2020-05-23 04:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200520_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='addetails',
            name='created_time',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.CreateModel(
            name='Expiredads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adid', models.CharField(max_length=128)),
                ('start_date', models.CharField(blank=True, max_length=128)),
                ('created_time', models.CharField(blank=True, max_length=128)),
                ('searched_date', models.DateField(default=django.utils.timezone.now)),
                ('adsid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Addetails')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Pagesdetail')),
            ],
        ),
    ]
