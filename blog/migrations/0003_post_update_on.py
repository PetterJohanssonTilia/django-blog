# Generated by Django 4.2.1 on 2024-07-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_excerpt"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="updated_on",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
