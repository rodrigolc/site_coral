from django.db import models
from django.urls import reverse
from model_utils.managers import InheritanceManager
# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=120)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateTimeField()
    data_editado = models.DateTimeField(auto_now=True)

    objects = InheritanceManager()

    def _str_(self):
        return self.titulo


class Livro(Post):
    editora = models.CharField(max_length=80)
    descricao = models.TextField()
    link_venda = models.URLField()
    imagem = models.ImageField(upload_to='books')

    def _str_(self):
        return self.titulo + '(' + self.editora + ')'

    def get_absolute_url(self):
        return reverse("detalhe_livro", kwargs={"livro_id": self.id})


class Texto(Post):
    descricao = models.TextField()
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='textos',blank=True)

    def get_absolute_url(self):
        return reverse("detalhe_texto", kwargs={"texto_id": self.id})


class Ilustracao(Post):
    imagem = models.ImageField

    def get_absolute_url(self):
        return reverse("detalhe_ilustra", kwargs={"ilustra_id": self.id})


class Poema(Texto):
    def get_absolute_url(self):
        return reverse("detalhe_poema", kwargs={"poema_id": self.id})


class Colecao(models.Model):
    nome = models.CharField(max_length=80)
    posts = models.ManyToManyField(Post)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateTimeField()
    data_editado = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("detalhe_colecao", kwargs={"id": self.id})


class Tag(models.Model):
    nome = models.CharField(max_length=80)
    posts = models.ManyToManyField(Post)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_editado = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("detalhe_tag", kwargs={"id": self.id})
