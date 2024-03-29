# Generated by Django 5.0.1 on 2024-01-10 16:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymgo', '0003_alter_usuario_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cargo',
            field=models.CharField(choices=[('Aluno', 'Aluno'), ('Gerente', 'Gerente'), ('Funcionario', 'Funcionario')], max_length=20),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('altura', models.DecimalField(decimal_places=2, help_text='Altura em metros', max_digits=5)),
                ('cep', models.IntegerField(blank=True, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plano_associacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('descriçao', models.CharField(max_length=300)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
