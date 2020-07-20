# Generated by Django 3.0.3 on 2020-07-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200719_0005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='specification',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo_3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo_4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo_5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo_6',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sub_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Earphones', 'Earphones'), ('Smartphone', 'Smartphone'), ('Laptops', 'Laptops'), ('Accessories', 'Accessories')], default='Accessories', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Dell', 'Dell'), ('Oneplus', 'Oneplus'), ('jbl', 'jbl'), ('Apple', 'Apple'), ('bose', 'bose'), ('Samsung', 'Samsung'), ('HP', 'HP'), ('Lenovo', 'Lenovo')], max_length=200),
        ),
        migrations.DeleteModel(
            name='Listing',
        ),
    ]
