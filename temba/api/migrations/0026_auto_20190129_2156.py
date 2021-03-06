# Generated by Django 2.1.5 on 2019-01-29 21:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0025_auto_20190129_2059")]

    operations = [
        migrations.RemoveField(model_name="webhookresult", name="created_by"),
        migrations.RemoveField(model_name="webhookresult", name="is_active"),
        migrations.RemoveField(model_name="webhookresult", name="modified_by"),
        migrations.RemoveField(model_name="webhookresult", name="modified_on"),
        migrations.AlterField(
            model_name="webhookresult",
            name="created_on",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False),
        ),
    ]
