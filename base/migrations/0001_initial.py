# Generated by Django 4.1 on 2024-03-09 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'admin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=20)),
                ('car_type', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=4)),
                ('color', models.CharField(max_length=20)),
                ('seat', models.PositiveIntegerField()),
                ('vehicle_no', models.CharField(max_length=15)),
                ('transmission', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=0, max_digits=6)),
                ('deposit', models.DecimalField(decimal_places=0, max_digits=6, null=True)),
                ('description', models.TextField(null=True)),
                ('status', models.CharField(default='A', max_length=15, null=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'car',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200)),
                ('id_card', models.CharField(max_length=200, null=True)),
                ('license_card', models.CharField(max_length=200, null=True)),
                ('phone_number', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(max_length=200, null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('approved_datetime', models.DateTimeField(null=True)),
                ('approved_by', models.ForeignKey(db_column='approved_by', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to='base.admin')),
            ],
            options={
                'db_table': 'customer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('pickup_location', models.CharField(max_length=100)),
                ('return_location', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=15)),
                ('transport_fee', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('damage_fee', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('late_fee', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('review', models.TextField(blank=True, null=True)),
                ('rating', models.PositiveIntegerField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(db_column='car_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='base.car')),
                ('customer', models.ForeignKey(db_column='customer_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='base.customer')),
            ],
            options={
                'db_table': 'order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('trading_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('province', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_account_name', models.CharField(blank=True, max_length=50, null=True)),
                ('id_card', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=15, null=True)),
                ('balance', models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('approved_datetime', models.DateTimeField(null=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('approved_by', models.ForeignKey(db_column='approved_by', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='providers', to='base.admin')),
            ],
            options={
                'db_table': 'provider',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=0, max_digits=6)),
                ('withdraw_datetime', models.DateTimeField(auto_now_add=True)),
                ('provider_id', models.ForeignKey(db_column='provider_id', on_delete=django.db.models.deletion.CASCADE, related_name='withdrawals', to='base.provider')),
            ],
            options={
                'db_table': 'withdrawal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('car', models.ForeignKey(db_column='car_id', on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='base.car')),
                ('customer_id', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to='base.customer')),
            ],
            options={
                'db_table': 'wishlist',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('reason', models.TextField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('car_id', models.ForeignKey(db_column='car_id', on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='base.car')),
                ('customer_id', models.ForeignKey(db_column='customer_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', to='base.customer')),
            ],
            options={
                'db_table': 'report',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('invoice_no', models.CharField(max_length=100)),
                ('payment_method', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=0, max_digits=6, null=True)),
                ('transaction_datetime', models.DateTimeField(auto_now_add=True)),
                ('deposit_return_time', models.DateTimeField(null=True)),
                ('refund_datetime', models.DateTimeField(null=True)),
                ('status', models.CharField(default='IN', max_length=15)),
                ('order', models.ForeignKey(db_column='order_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='base.order')),
            ],
            options={
                'db_table': 'payment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(db_column='customer_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_rooms', to='base.customer')),
                ('provider', models.ForeignKey(db_column='provider_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_rooms', to='base.provider')),
            ],
            options={
                'db_table': 'chat_room',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('file_path', models.CharField(max_length=200, null=True)),
                ('is_read', models.BooleanField(default=False)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('chat_room_id', models.ForeignKey(db_column='chat_room_id', on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='base.chatroom')),
            ],
            options={
                'db_table': 'chat',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CarFile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('file_path', models.CharField(max_length=200)),
                ('file_type', models.CharField(max_length=5)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('car_id', models.ForeignKey(db_column='car_id', on_delete=django.db.models.deletion.CASCADE, related_name='car_files', to='base.car')),
            ],
            options={
                'db_table': 'car_file',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='car',
            name='provider',
            field=models.ForeignKey(db_column='provider_id', on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='base.provider'),
        ),
        migrations.AddField(
            model_name='car',
            name='updated_by',
            field=models.ForeignKey(db_column='updated_by', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='base.admin'),
        ),
    ]
