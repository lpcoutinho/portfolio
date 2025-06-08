from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField(verbose_name='Conteúdo')
    excerpt = models.TextField(max_length=300, verbose_name='Resumo', 
                              help_text='Breve descrição do post (máx. 300 caracteres)')
    
    # Metadata
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    published = models.BooleanField(default=True, verbose_name='Publicado')
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True, 
                                       verbose_name='Meta Description')
    
    # Tags simples (sem model separado por simplicidade)
    tags = models.CharField(max_length=200, blank=True, 
                           help_text='Tags separadas por vírgula (ex: django, python, ai)')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post do Blog'
        verbose_name_plural = 'Posts do Blog'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
    
    def get_tags_list(self):
        """Retorna lista de tags"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []
    
    def reading_time(self):
        """Calcula tempo estimado de leitura (250 palavras por minuto)"""
        word_count = len(self.content.split())
        return max(1, round(word_count / 250))