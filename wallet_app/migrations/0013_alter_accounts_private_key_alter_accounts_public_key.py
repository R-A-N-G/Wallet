# Generated by Django 4.0 on 2022-01-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0012_alter_accounts_private_key_alter_accounts_public_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='private_key',
            field=models.CharField(default=b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDlygNUwmp311IIHfq/Ch8FHdwYBgiJHPeVaAfbIIEAVYakJwcE\nG3wTg6rivw2sVZwA080m9WFFi6HnBY5NBzwmwrFjzLNMnqZnl81NMGe5iWq+qG9l\nje/ZpysSyk//CBuAxQxvbN4Iia1QaoGNYhdFErqpe5BnFbSRVZS5774/hQIDAQAB\nAoGAZeaANKmkejGHpKbax7YOzH+R1ytxxJAOcPh5p2BSJJpIw2m1MEqZ6rN0Z+oO\nf7JVJH7IVrLxKFyD9wVdNeZz8us2S9P+ne7C1Omo/+9hOACgx/GIVfLC9v/2k1QN\nK9o0Dftg0CzntNylMFoYW8r1hVhOVykniA0y5eveA7Iokg8CQQDunvG4H++/PSn6\nBPId45KNYRrsN8ArJfh77SuKbMSTYPGv2baN6pdXuIgKKGsP/ZTrgraG0LDtUjDt\nDYvMLcNbAkEA9oZm1omBsHe89T1Xiog1rboH/fHXqh8VNxWVcoYb6utCkmaoPiRj\no9eXTjfdbiPHszrKROfMNUNNngKSEQvenwJBANRiPezO6BnDu8fffQwjUH5rjoXu\n/SiqbCcJKnbTZodygssssPJReZDHGrZH0TrzTgfsWL9XohIo1Ik5RFNf6/8CQQCd\n6phjoy/VV85OFh5GmlwwTfOio1GwIzsWzxetheTKRiud1m69Z9f/8zF0JGsOi5L3\n55f8LbPtBpDov+LLUpwnAkApXr8DAECLKUxbe7953+utMYnMyXa7abS7TYP2V9+l\ntGWCXM93pXe0t8wFyXQlFTFL27PodJWGosYiJwCxh5NH\n-----END RSA PRIVATE KEY-----', max_length=1024),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='public_key',
            field=models.CharField(default=b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+sg2d1Wh5IN1rkLHDar2snZSC\nsj8tkWOYLxjRgulQDuPva0xB3rIT97DzLpPy9qIAhaEufTKYQTxg48/EyD7uK/El\njN0mkvaaggb07/12W6KGnTyNRvQvNACnGeKUklvz6XDOUyNCcxujGd+SyyJx/Z/m\nVUalS5i+SXFz81C/QwIDAQAB\n-----END PUBLIC KEY-----', max_length=1024),
        ),
    ]