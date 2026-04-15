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
            {'arquivo': 'antes-e-depois.webp', 'titulo': 'Foto de Antes e Depois'},
            {'arquivo': 'avatar-ia-feminio.webp', 'titulo': 'Avatar de IA Feminino'},
            {'arquivo': 'com-produto.webp', 'titulo': 'Com produto'},
            {'arquivo': 'com-roupa.webp', 'titulo': 'Com roupa'},
            {'arquivo': 'empresas.webp', 'titulo': 'Para Empresas'},
            {'arquivo': 'iphone-15-pro-max.webp', 'titulo': 'Foto Estilo iPhone'},
            {'arquivo': 'lifestyle.webp', 'titulo': 'Lifestyle Aspiracional'},
            {'arquivo': 'mockup.webp', 'titulo': 'Mockup de Produto Digital'},
            {'arquivo': 'para-anuncios.webp', 'titulo': 'Imagem para Anúncio Meta'},
            {'arquivo': 'para-vitrine.webp', 'titulo': 'Foto de Produto Premium'},
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
