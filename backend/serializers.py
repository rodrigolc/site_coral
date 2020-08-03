from rest_framework import serializers
from .models import Post, Livro, Texto, Ilustracao, Poema, Colecao, Tag


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class TextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Texto
        fields = "__all__"


class IlustracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ilustracao
        fields = "__all__"


class PoemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poema
        fields = "__all__"


class ColecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colecao
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"