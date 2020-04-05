from django.contrib import admin

# Register your models here.

from .models import Post,Colecao,Ilustracao,Livro,Poema,Texto # add this

class PostAdmin(admin.ModelAdmin):  # add this
    list_display = ('titulo','data_criacao','data_publicacao','data_editado')



class ColecaoAdmin(admin.ModelAdmin):  # add this
    def colecao_post_count(self, obj):
        return obj.posts.count()
    colecao_post_count.short_description = "Posts Count"
    list_display = ('nome','colecao_post_count','data_criacao','data_publicacao','data_editado')


class IlustracaoAdmin(admin.ModelAdmin):  # add this
    list_display = ('titulo','data_criacao','data_publicacao','data_editado' ) # add this

class LivroAdmin(admin.ModelAdmin):  # add this
    list_display = ('titulo','editora','descricao','link_venda')

class PoemaAdmin(admin.ModelAdmin):  # add this
    list_display = ('titulo','data_criacao','data_publicacao','data_editado') # add this

class TextoAdmin(admin.ModelAdmin):  # add this
    list_display = ('titulo','data_criacao','data_publicacao','data_editado') # add this
# Register your models here.

admin.site.register(Post,PostAdmin)
admin.site.register(Colecao,ColecaoAdmin)
admin.site.register(Ilustracao,IlustracaoAdmin)
admin.site.register(Livro,LivroAdmin)
admin.site.register(Poema,PoemaAdmin)
admin.site.register(Texto,TextoAdmin)