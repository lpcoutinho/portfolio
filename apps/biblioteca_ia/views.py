from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from .models import Categoria, Prompt


def biblioteca_home(request):
    """Página inicial da biblioteca com todas as categorias."""
    categorias = Categoria.objects.prefetch_related(
        'prompts'
    ).annotate(
        total_prompts=Count('prompts', filter=Q(prompts__ativo=True))
    ).filter(total_prompts__gt=0).order_by('ordem', 'nome')

    total_prompts = Prompt.objects.filter(ativo=True).count()

    context = {
        'categorias': categorias,
        'total_prompts': total_prompts,
    }
    return render(request, 'biblioteca_ia/home.html', context)


def categoria_detalhe(request, slug):
    """Página de detalhes de uma categoria com seus prompts."""
    categoria = get_object_or_404(Categoria, slug=slug)
    prompts = categoria.prompts.filter(ativo=True).order_by('ordem', 'titulo')

    # Mapeamento de imagens estáticas para a categoria Imagens Ultra Realistas
    galeria_imagens = []
    if categoria.nome == 'Imagens Ultra Realistas':
        galeria_imagens = [
            {'arquivo': 'antes-e-depois.png', 'titulo': 'Foto de Antes e Depois'},
            {'arquivo': 'avatar-ia-feminio.png', 'titulo': 'Avatar de IA Feminino'},
            {'arquivo': 'com-produto.png', 'titulo': 'Com produto'},
            {'arquivo': 'com-roupa.png', 'titulo': 'Com roupa'},
            {'arquivo': 'empresas.png', 'titulo': 'Para Empresas'},
            {'arquivo': 'iphone-15-pro-max.png', 'titulo': 'Foto Estilo iPhone'},
            {'arquivo': 'lifestyle.png', 'titulo': 'Lifestyle Aspiracional'},
            {'arquivo': 'mockup.png', 'titulo': 'Mockup de Produto Digital'},
            {'arquivo': 'para-anuncios.png', 'titulo': 'Imagem para Anúncio Meta'},
            {'arquivo': 'para-vitrine.png', 'titulo': 'Foto de Produto Premium'},
        ]

    context = {
        'categoria': categoria,
        'prompts': prompts,
        'galeria_imagens': galeria_imagens,
    }
    return render(request, 'biblioteca_ia/categoria.html', context)


def prompt_detalhe(request, slug, pk):
    """Página de detalhes de um prompt."""
    categoria = get_object_or_404(Categoria, slug=slug)
    prompt = get_object_or_404(
        Prompt,
        pk=pk,
        categoria=categoria,
        ativo=True
    )

    # Prompts relacionados da mesma categoria
    prompts_relacionados = categoria.prompts.filter(
        ativo=True
    ).exclude(pk=pk)[:3]

    context = {
        'categoria': categoria,
        'prompt': prompt,
        'prompts_relacionados': prompts_relacionados,
    }
    return render(request, 'biblioteca_ia/prompt.html', context)
