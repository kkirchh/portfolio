# Generated by Django 4.1.4 on 2022-12-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='facebook_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='instagram_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='linkedin_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='twitter_link',
            field=models.URLField(null=True),
        ),
    ]
