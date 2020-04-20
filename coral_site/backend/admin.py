from django.contrib import admin

# Register your models here.

from .models import Post, Colecao, Ilustracao, Livro, Poema, Texto


class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao',
                    'data_publicacao', 'data_editado')


class ColecaoAdmin(admin.ModelAdmin):
    # shortcut para conseguir ter o numero de posts no admin
    def colecao_post_count(self, obj):
        return obj.posts.count()
    colecao_post_count.short_description = "Numero de Posts"
    list_display = ('nome', 'colecao_post_count', 'data_criacao',
                    'data_publicacao', 'data_editado')


class IlustracaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao',
                    'data_publicacao', 'data_editado')


class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'descricao', 'link_venda')


class PoemaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao',
                    'data_publicacao', 'data_editado')


class TextoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao',
                    'data_publicacao', 'data_editado')

# Register your models here.


admin.site.register(Post, PostAdmin)
admin.site.register(Colecao, ColecaoAdmin)
admin.site.register(Ilustracao, IlustracaoAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Poema, PoemaAdmin)
admin.site.register(Texto, TextoAdmin)
