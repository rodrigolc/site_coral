from django.db import models
import time

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=120)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateTimeField()
    data_editado = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.titulo


class Livro(Post):
    editora = models.CharField(max_length=80)
    descricao = models.TextField()
    link_venda = models.URLField()

    def _str_(self):
        return self.titulo + '(' + self.editora + ')'


class Texto(Post):
    conteudo = models.TextField()


class Ilustracao(Post):
    imagem = models.ImageField


class Poema(Texto):
    pass


class Colecao(models.Model):
    nome = models.CharField(max_length=80)
    posts = models.ManyToManyField(Post)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateTimeField()
    data_editado = models.DateTimeField(auto_now=True)
