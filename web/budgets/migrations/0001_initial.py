# Generated by Django 2.1.2 on 2018-10-03 03:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled', max_length=180)),
                ('total_budget', models.FloatField()),
                ('remaining_budget', models.FloatField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budgets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.FloatField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('type', models.CharField(choices=[('WITHDRAWAL', 'Withdrawal'), ('DEPOSIT', 'Deposit')], default='Withdrawal', max_length=16)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='budgets.Budget')),
            ],
        ),
    ]