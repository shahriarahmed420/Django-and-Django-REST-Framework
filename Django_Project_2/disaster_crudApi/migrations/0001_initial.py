# Generated by Django 5.1.3 on 2024-11-29 05:48

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
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('category', models.CharField(choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Home & Kitchen', 'Home & Kitchen'), ('Books', 'Books'), ('Sports', 'Sports')], max_length=50)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]