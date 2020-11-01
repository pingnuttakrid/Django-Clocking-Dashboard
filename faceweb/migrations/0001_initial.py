# Generated by Django 3.0.5 on 2020-10-21 14:03

from django.db import migrations, models
import django.db.models.deletion
import faceweb.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clocking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_id', models.CharField(max_length=10, unique=True)),
                ('door', models.CharField(max_length=2)),
                ('temp', models.FloatField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Image_Clocking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(default='none/no-img.jpg', null=True, upload_to='clocking')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Threshold_Clocking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Threshold_Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=5)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('nation', models.CharField(max_length=20)),
                ('Type', models.CharField(max_length=30)),
                ('idtype', models.CharField(max_length=255)),
                ('idno', models.CharField(max_length=13)),
                ('birthday', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=10)),
                ('adresss', models.CharField(max_length=300)),
                ('adcontact', models.CharField(max_length=10)),
                ('overseaadresss', models.CharField(max_length=300)),
                ('ovcontact', models.CharField(max_length=10)),
                ('emerseaadresss', models.CharField(max_length=300)),
                ('emercontact', models.CharField(max_length=10)),
                ('imgprofile', models.ImageField(default='none/no-img.jpg', null=True, upload_to=faceweb.models.upload_path_handler)),
                ('imgstraight', models.ImageField(default='none/no-img.jpg', null=True, upload_to=faceweb.models.upload_path_handler)),
                ('imgtop', models.ImageField(default='none/no-img.jpg', null=True, upload_to=faceweb.models.upload_path_handler)),
                ('imgbottom', models.ImageField(default='none/no-img.jpg', null=True, upload_to=faceweb.models.upload_path_handler)),
                ('imgleft', models.ImageField(default='none/no-img.jpg', null=True, upload_to=faceweb.models.upload_path_handler)),
                ('imgright', models.ImageField(default='none/no-img.jpg', null=True, upload_to=faceweb.models.upload_path_handler)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faceweb.Status')),
            ],
        ),
    ]