# Generated by Django 2.2 on 2019-05-09 18:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0002_auto_20190507_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to='djangobin.Author'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to='djangobin.Language'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='tags',
            field=models.ManyToManyField(related_name='snippets', to='djangobin.Tag'),
        ),
    ]