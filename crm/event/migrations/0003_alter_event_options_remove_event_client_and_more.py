# Generated by Django 4.0.4 on 2022-06-04 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_alter_contract_options_remove_contract_payment_due_and_more'),
        ('event', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-date_updated', '-date_created']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='client',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AddField(
            model_name='event',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='contract',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='event', serialize=False, to='contract.contract'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_updated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
