# Generated by Django 4.1.4 on 2022-12-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/')),
                ('full_name', models.CharField(default='Jasur Juraev', max_length=300)),
                ('birthday', models.CharField(default='26 January 2005', max_length=200)),
                ('web_site', models.CharField(default='www.jasur.com', max_length=155)),
                ('phone', models.CharField(default='+998 (94) 800 2005', max_length=200)),
                ('city', models.CharField(default='Tashkent, UZB', max_length=200)),
                ('age', models.IntegerField(default=17)),
                ('degree', models.CharField(default='Junior', max_length=100)),
                ('email', models.CharField(default='jasurkkirchh@gmail.com', max_length=300)),
                ('freelance', models.BooleanField(default=True)),
                ('description', models.TextField(default='I am a backend engineer with strong and high quality knowledge. With 1+ years of experience in coding. Ready to learn new technologies and frameworks for work')),
                ('instagram_link', models.URLField(default=None)),
                ('facebook_link', models.URLField(default=None)),
                ('twitter_link', models.URLField(default=None)),
                ('linkedin_link', models.URLField(default=None)),
            ],
        ),
    ]
