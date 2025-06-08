from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    """
    Converte texto Markdown para HTML
    """
    if not text:
        return ''
    
    # Configurar extensões do Markdown
    md = markdown.Markdown(
        extensions=[
            'extra',  # Inclui fenced_code, tables, etc
            'codehilite',  # Highlight de código
            'nl2br',  # Quebras de linha automáticas
        ],
        extension_configs={
            'codehilite': {
                'css_class': 'highlight',
                'use_pygments': False,  # Usar CSS personalizado
            }
        }
    )
    
    return mark_safe(md.convert(text))