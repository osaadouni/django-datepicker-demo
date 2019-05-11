# Generated by Django 2.2 on 2019-05-07 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField()),
                ('last_logged_in', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lang_code', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('mime', models.CharField(help_text='MIME to use when sending snippet as file.', max_length=100)),
                ('file_extension', models.CharField(max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('original_code', models.TextField()),
                ('highlighted_code', models.TextField()),
                ('expiration', models.CharField(choices=[('never', 'Never'), ('1 week', '1 week'), ('1 month', '1 month'), ('6 month', '6 month'), ('1 year', '1 year')], max_length=10)),
                ('exposure', models.CharField(choices=[('public', 'Public'), ('unlisted', 'Unlist'), ('private', 'Private')], max_length=10)),
                ('hits', models.IntegerField(default=0)),
                ('slug', models.SlugField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangobin.Author')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangobin.Language')),
                ('tags', models.ManyToManyField(to='djangobin.Tag')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.AddIndex(
            model_name='language',
            index=models.Index(fields=['lang_code'], name='language_code'),
        ),
        migrations.AddIndex(
            model_name='author',
            index=models.Index(fields=['active'], name='djangobin_a_active_80decf_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together={('name', 'email')},
        ),
    ]
