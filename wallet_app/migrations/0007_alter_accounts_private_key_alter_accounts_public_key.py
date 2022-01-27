# Generated by Django 4.0 on 2022-01-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0006_remove_accounts_key_pair_accounts_private_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='private_key',
            field=models.CharField(default='-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCazj+rpcT4SgZDKQ6YvwsIhCwqVwDB6ww5F0Vp3diwTWdfN19b\ncDxBkNXaKmfY4RfnmcoJuBHwiyEL+3JqIyr95ZZy3yIwqZsNUywXNex+00gq6Y2l\nMfgexkfuwy0GY1MyPwyRPiVtOYT4ePvRvqDUZq1xOLEIGWn8chpakyZWPQIDAQAB\nAoGAFjVkmQFtIpmsEFKBj5RIxu3/UAuvRiKsXDxkbu2uuoxAOj69ZWbSni1jIKtY\nvpp8TXOYspA/spyjHw7xuRxWfGECva1NWMzdNbuopmOeHDgJ5w9j1Rbd49dtno5X\ndv0Do4C/UZbvVbEoRgLgAQIw01CRcjWlGhf/3cspooweP9kCQQC5iSjxVvisVMaG\npKlFXNYPcRBVakFMmvdkQevr/Ee/uvCcUJz9Mlr+shO03jvYE4sG+nvr214hPo9I\nsCcb/s6rAkEA1ZlVCW4KdT3trziTPDAJv3r860x96DkxedXtKv+WtZpPyKsCS+yu\nx2CAzqARBXzariZwc3aJGibNoXPZBRnOtwJASz4Wvpk4zBqtUFli1GBr52NA7oLi\n7IBEKAKb/N4Y8uaLQblnkT9kq7noSAeAWYbDcRcQPnx+Vhka3q2hjrbtdQJAAReC\njsTIOucxItcoMYORWTA4wL8oWZqJPTUxvCmITK9YPw9YuKiiEBTXM7cvvxZvS7qY\nko6FjuOp42xjLJqAKwJBAK1Pq5rsNOcyrBwTOL7GxvWbeTsIS3HkHZqgYIqbirJf\nzVdMGI32wf7xoxnHIiOAchc1Dqvgc8C+uXmnbjLAfdA=\n-----END RSA PRIVATE KEY-----', max_length=1024),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='public_key',
            field=models.CharField(default='-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCazj+rpcT4SgZDKQ6YvwsIhCwq\nVwDB6ww5F0Vp3diwTWdfN19bcDxBkNXaKmfY4RfnmcoJuBHwiyEL+3JqIyr95ZZy\n3yIwqZsNUywXNex+00gq6Y2lMfgexkfuwy0GY1MyPwyRPiVtOYT4ePvRvqDUZq1x\nOLEIGWn8chpakyZWPQIDAQAB\n-----END PUBLIC KEY-----', max_length=1024),
        ),
    ]
