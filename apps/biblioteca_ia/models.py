from django.db import models


class Categoria(models.Model):
    """Categorias para organizar os prompts."""
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    icone = models.CharField(max_length=50, help_text="Emoji ou nome do ícone")
    descricao = models.TextField(blank=True)
    ordem = models.PositiveIntegerField(default=0, help_text="Ordem de exibição")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ordem', 'nome']
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.nome)
        # Garante que o slug nunca seja vazio
        if not self.slug:
            self.slug = f"categoria-{self.pk or 'temp'}"
        super().save(*args, **kwargs)


class Prompt(models.Model):
    """Prompts para uso com Inteligência Artificial."""
    titulo = models.CharField(max_length=200)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='prompts'
    )
    conteudo = models.TextField(help_text="O texto completo do prompt")
    descricao_curta = models.CharField(
        max_length=300,
        blank=True,
        help_text="Descrição breve para preview"
    )
    # Campos estruturados
    para_que_serve = models.TextField(blank=True, help_text="Para que serve este prompt")
    como_usar = models.TextField(blank=True, help_text="Como usar o prompt")
    resultado_esperado = models.TextField(blank=True, help_text="Resultado esperado")
    exemplo_resultado = models.TextField(blank=True, help_text="Exemplo de resultado")
    ordem = models.PositiveIntegerField(default=0, help_text="Ordem de exibição na categoria")
    imagem = models.ImageField(
        upload_to='biblioteca_ia/prompts/',
        blank=True,
        null=True,
        help_text="Imagem de exemplo (opcional)"
    )
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['categoria', 'ordem', 'titulo']
        verbose_name = 'prompt'
        verbose_name_plural = 'prompts'

    def __str__(self):
        return self.titulo
