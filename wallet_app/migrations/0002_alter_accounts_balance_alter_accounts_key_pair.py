# Generated by Django 4.0 on 2022-01-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='balance',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='key_pair',
            field=models.CharField(default='-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDFHXvS107NFIf+P1j7O8wewpYu61t+YbO/s0FYK+Mn3tiPqC7+\n4BYFgQ1qTGNqXoeGIiUNyAqKhc+h95LKh5CcwR4gwImpvJYcNJrPMhoxv9wmzMre\nEYTSK1QiyiuHk2rwlZY5i5ga3Xryfdx6sALdJ3xmfbQSELt39Wp4IgmtJQIDAQAB\nAoGAEVTy1sqkvKaSAJqMVebfn1LHxs9eB6JKnlACLmEJg692Bkeo/jMw7IH47oBR\n+3/dVb9515jfyGdUpu6wYwuBfQdopfB9EOm1suVDTV7JlplJ8EqOQj/GTY5mFhl8\nxs9Rc+IUsD5E1eegQc8k7UIPJgIVbCG45sSHSL6vDkjFZ08CQQDQ/+O+PuFuWTKg\nbBrdXlmwL75TRzrUszIkowkPN0MA/mXPBPLxUpvmUuxJn+05H1QQwtVSStADlE+W\nhHSjFDwXAkEA8XFose0/6Hol1+Cqa5H0w+1JmXQkVeqwO3wZ8vrUXzwLB5SdkRgb\noetjAzmf99ZFh63Ommfs+vVjrgGgFIH6IwJBAKWfUvwtWnoXB46nfLaWkV6Uxy+5\nj76E7ySnaoN7WIbOEyH2GwvwWgkxB3zk1png4L6Tl3cqQCPGATgXaVLesysCQQDK\nxmWYcVooJFYeHWjjmRyJZINYpstRgR5rhwnAINs19JaK0k0XK7khXzCz57SrEEEq\n91U6JqhICMmjvWe1cYgjAkA8am5KUJjwFADxIEmonP71DWgTTbOExkCJ7VK7XySC\nZ/wnKGlxkO1x/u3C7yYVdjgWCLaYQkkri8UwLoF/JRDl\n-----END RSA PRIVATE KEY-----|<built-in method decode of bytes object at 0x000002558D956500>', max_length=1024, unique=True),
        ),
    ]