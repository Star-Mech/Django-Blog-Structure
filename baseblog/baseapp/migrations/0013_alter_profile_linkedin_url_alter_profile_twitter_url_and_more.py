# Generated by Django 4.0.4 on 2022-05-29 10:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baseapp', '0012_profile_linkedin_url_profile_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='linkedin_url',
            field=models.CharField(blank=True, default='#', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_url',
            field=models.URLField(blank=True, default='#', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank=True, default='#', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', ckeditor.fields.RichTextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseapp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
