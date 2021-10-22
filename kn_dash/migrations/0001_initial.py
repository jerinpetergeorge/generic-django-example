# Generated by Django 3.2.7 on 2021-10-22 14:51

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('transaction_id', models.CharField(max_length=120, verbose_name='Transaction ID')),
                ('transaction_created', models.DateTimeField(verbose_name='Created')),
                ('state', models.CharField(choices=[('created', 'Created'), ('pending', 'Pending'), ('attempted', 'Attempted'), ('paid', 'Paid'), ('canceled', 'Canceled'), ('expired', 'Expired'), ('invalid', 'Invalid')], default='pending', max_length=120, verbose_name='state')),
                ('type', models.CharField(choices=[('e_commerce', 'E-Commerce'), ('payment_request', 'Payment request'), ('customer_payment', 'Customer payment'), ('third_party', 'Third party')], default='e_commerce', max_length=24, verbose_name='Type')),
                ('gateway_code', models.CharField(blank=True, db_index=True, default='', max_length=16, verbose_name='Gateway code')),
                ('fee', models.CharField(default='0', max_length=24, verbose_name='Fee')),
                ('amount', models.CharField(default='0', max_length=24, verbose_name='Amount')),
                ('total', models.CharField(default='0', max_length=24, verbose_name='Total')),
                ('currency_code', models.CharField(max_length=3, verbose_name='Currency code')),
                ('state_changed_at', models.DateTimeField(null=True, verbose_name='State changed at')),
            ],
            options={
                'verbose_name': 'Payment transaction',
                'verbose_name_plural': 'Payment transactions',
                'ordering': ('-created', '-modified'),
            },
        ),
    ]