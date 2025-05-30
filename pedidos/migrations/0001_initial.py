# Generated by Django 5.1.2 on 2025-03-03 01:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PEDIDO',
            fields=[
                ('idPedido', models.AutoField(primary_key=True, serialize=False)),
                ('mesa', models.IntegerField()),
                ('estatus', models.IntegerField(choices=[(1, 'CREADO'), (2, 'ACEPTADO'), (3, 'LISTO PARA ENTREGA'), (4, 'ENTREGADO')], default=1)),
                ('fechaRegistro', models.DateTimeField(auto_now_add=True)),
                ('nota_cocina', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCTOS',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='DETALLE_PEDIDO',
            fields=[
                ('idDetallePedido', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='pedidos.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.productos')),
            ],
        ),
        migrations.CreateModel(
            name='USUARIO',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apPaterno', models.CharField(max_length=50)),
                ('apMaterno', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15, unique=True)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('cuenta', models.CharField(max_length=50, unique=True)),
                ('contrasena', models.CharField(max_length=25)),
                ('rol', models.IntegerField(choices=[(1, 'MESERO'), (2, 'COCINA'), (3, 'ADMINISTRADOR')])),
                ('fechaRegistro', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='idUsuarioRegistro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedidos.usuario'),
        ),
        migrations.AddConstraint(
            model_name='usuario',
            constraint=models.UniqueConstraint(fields=('cuenta',), name='unique_cuenta'),
        ),
        migrations.AddConstraint(
            model_name='usuario',
            constraint=models.UniqueConstraint(fields=('telefono',), name='unique_telefono'),
        ),
        migrations.AddConstraint(
            model_name='usuario',
            constraint=models.UniqueConstraint(fields=('correo',), name='unique_correo'),
        ),
    ]
