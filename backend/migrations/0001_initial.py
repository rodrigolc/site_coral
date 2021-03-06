# Generated by Django 3.0.5 on 2020-08-03 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_publicacao', models.DateTimeField()),
                ('data_editado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ilustracao',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Post')),
            ],
            bases=('backend.post',),
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Post')),
                ('editora', models.CharField(max_length=80)),
                ('descricao', models.TextField()),
                ('link_venda', models.URLField()),
                ('imagem', models.ImageField(upload_to='books')),
            ],
            bases=('backend.post',),
        ),
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Post')),
                ('descricao', models.TextField()),
                ('conteudo', models.TextField()),
                ('imagem', models.ImageField(blank=True, upload_to='textos')),
            ],
            bases=('backend.post',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_editado', models.DateTimeField(auto_now=True)),
                ('posts', models.ManyToManyField(to='backend.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Colecao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_publicacao', models.DateTimeField()),
                ('data_editado', models.DateTimeField(auto_now=True)),
                ('posts', models.ManyToManyField(to='backend.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Poema',
            fields=[
                ('texto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.Texto')),
            ],
            bases=('backend.texto',),
        ),
    ]
