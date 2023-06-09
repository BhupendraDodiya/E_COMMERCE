# Generated by Django 4.1.5 on 2023-03-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('mobile', 'mobile'), ('laptop', 'laptop'), ('top wear', 'top wear'), ('bottom wear', 'bottom wear')], max_length=100)),
                ('product_image', models.ImageField(upload_to='product/')),
            ],
        ),
    ]
