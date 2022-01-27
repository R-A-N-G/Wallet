# Generated by Django 4.0 on 2022-01-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0004_alter_accounts_private_key_alter_accounts_public_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='private_key',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='public_key',
        ),
        migrations.AddField(
            model_name='accounts',
            name='key_pair',
            field=models.CharField(default='-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQDpW9ZYFfM9RTQWi1Uox1lWYtFmVwMHxzwS/43tBQUNVBoAAvmA\n7/MC54L/S1VfeZTTe4h/xwvA9E8fXdx4H+Tl14oUAPYwZzSu4v4rgzEQ/oYZ6lhG\nyQ1ZSt+4C8lOe4JcLax0ZNWUn1Xy+654iUlVYUEXJrSeknRMG/HD3i8g3wIDAQAB\nAoGAbJoU8wGkJgui5isKAuRjq1Rp55rvChuq1ZyhTIFdjIprXz4DKAKDsgJUcMN6\ng+htXs7LA8x6p94LRKnGBRGy0HEyFZ1qlPQYQce3VZle628lmMSqVpDItWtPRZj9\nSepJZXjuU9aNlZJtcN+J7BIdEanqXS12q2XfWnE+t6oKReECQQDzED0arG/v6wZb\n/vH3NwnriE1R6Xkhz/44UCow4vcMe8KiehC+ALS2papfXrEQCi0XM4MiI4jRlKR3\nG0eB6L9bAkEA9cdfC57XaHAePLjxoDeg9YFGWTiN+KDqxKFXMd18vNsF5nxP773o\nvR4+XMQ/+DaQein9PU7FAQKRpecHr2u/zQJAIUWIx7zw+at3TGKCpq9/CSG4S80k\nyq8ZAoZesCBxZuEODIWfAxM/qXzV7IYewK5T68geXC73DJFHThKK4EqG3wJAb4VE\nejhb03a0MadVc/Zp4ZwD+K3xtXQGsqvmrairVeIn3jpf5w+L0Gwtrdgakpznl5b/\n4lagi2HIBrg6w30nrQJBAI77fWrSFoGbTAaNhz6kjP184AmVe5PdEVsBYTS9nUMQ\nsgI8DxwG4hUbn7/b34fKiybScQ6CVruq6sPhhIpVl7A=\n-----END RSA PRIVATE KEY-----|-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDpW9ZYFfM9RTQWi1Uox1lWYtFm\nVwMHxzwS/43tBQUNVBoAAvmA7/MC54L/S1VfeZTTe4h/xwvA9E8fXdx4H+Tl14oU\nAPYwZzSu4v4rgzEQ/oYZ6lhGyQ1ZSt+4C8lOe4JcLax0ZNWUn1Xy+654iUlVYUEX\nJrSeknRMG/HD3i8g3wIDAQAB\n-----END PUBLIC KEY-----', max_length=1024, unique=True),
        ),
    ]