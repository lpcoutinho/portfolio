from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost


def blog_list(request):
    """Lista de posts do blog"""
    posts = BlogPost.objects.filter(published=True)
    
    # Paginação (6 posts por página)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
        'page_obj': page_obj,
    }
    return render(request, 'blog/blog_list.html', context)


def post_detail(request, slug):
    """Detalhe de um post específico"""
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    
    # Posts relacionados (mesmo tag ou mais recentes)
    related_posts = BlogPost.objects.filter(
        published=True
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)