# Generated by Django 4.1.4 on 2023-02-11 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myPhotoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='photo',
            name='date_creation',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myPhotoApp.categorie'),
        ),
    ]
