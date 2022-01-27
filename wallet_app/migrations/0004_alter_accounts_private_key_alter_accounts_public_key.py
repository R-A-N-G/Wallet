# Generated by Django 4.0 on 2022-01-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0003_remove_accounts_key_pair_accounts_private_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='private_key',
            field=models.CharField(default='-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC4RzkddZXjzNJ8K6fJUlIif6PpZdkCS4F6QbpZ9DnZuqvHcmEh\nXkVzGP6uZola527xDUCg5mu/QXcFpGs3EZZqsbqkS35uigfwt2SHn4BdxIZsLi6R\nfcHYPcuO+EvNpehmFztYDTePPTK+WL5HcCAGCkp9Gfhc6+n0JrNitDKUFwIDAQAB\nAoGAJ8nlGKnHa/DRL9NjPpJiPqWtuBrwENFJyyJ/AKY9iXgHWCCnvUM0HqZycyib\nlr+q0ixo3HT0Jc8WSmcWaUUIY3GWChcPcdyreJNjY2OQTYpmgD1i02uF3Ko1FbbQ\n0KKJ474uDAlw4G7o/fc0MxaM4JhFOBUq/cPJFBW3txV8kvUCQQC+qn9WaFkNcjyz\nh9JzszHvGnD7e1XQ68TRD1B8dSruVnTycYyTg4TVkrO39OJr5EhcF+4mCHhvUg5Q\n4XCNoId7AkEA92xhG+HdcB0oJ4ClO8y3kRKGz2Vqy+cfm6HgpXTvTxe/qbVWuU34\n4NQn0uMrWKEtBTFLcD2YeKuenR3jL4E1FQJAUmuNhCKzbDaXutvZw54Q1dVORce4\n/wkMGXtPRZ24ozLIdw1SwWm3AEPcYIcBYbZa+UR29AXxWd3Uxm3No8tjBQJAeCRh\nVxeq3fjaeawHD+2NKV2Upnp5jD9TYtAM9Gq+lWpTwAV08hABjLKYD9gNQUEqSj4w\ngnT2Z4n2QBa2LWgRLQJBALpR6K0Z6nNBYHSKdz1B61JjiuzXP+eIeNVdzuT57EPe\nv5CSPCW2XomwEWXCpyYuz6BM/Yaky3jpXeSoO7daNPo=\n-----END RSA PRIVATE KEY-----', max_length=1024, unique=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='public_key',
            field=models.CharField(default='-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4RzkddZXjzNJ8K6fJUlIif6Pp\nZdkCS4F6QbpZ9DnZuqvHcmEhXkVzGP6uZola527xDUCg5mu/QXcFpGs3EZZqsbqk\nS35uigfwt2SHn4BdxIZsLi6RfcHYPcuO+EvNpehmFztYDTePPTK+WL5HcCAGCkp9\nGfhc6+n0JrNitDKUFwIDAQAB\n-----END PUBLIC KEY-----', max_length=1024, unique=True),
        ),
    ]
