from django.contrib import admin
from .models import Categoria, Prompt


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'icone', 'ordem', 'criado_em']
    list_editable = ['icone', 'ordem']
    search_fields = ['nome']
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ['ordem', 'nome']


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'ativo', 'ordem', 'criado_em']
    list_filter = ['categoria', 'ativo', 'criado_em']
    list_editable = ['ativo', 'ordem']
    search_fields = ['titulo', 'conteudo']
    ordering = ['categoria', 'ordem', 'titulo']
    date_hierarchy = 'criado_em'
    readonly_fields = ['criado_em', 'atualizado_em']

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'categoria', 'ativo')
        }),
        ('Conteúdo', {
            'fields': ('conteudo', 'descricao_curta')
        }),
        ('Detalhes Estruturados', {
            'fields': ('para_que_serve', 'como_usar', 'resultado_esperado', 'exemplo_resultado'),
            'classes': ('collapse',)
        }),
        ('Mídia', {
            'fields': ('imagem',)
        }),
        ('Organização', {
            'fields': ('ordem',)
        }),
        ('Metadados', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
