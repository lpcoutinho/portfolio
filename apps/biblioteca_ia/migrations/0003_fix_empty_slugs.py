# Generated to fix empty slugs in existing categories

from django.db import migrations
from django.utils.text import slugify


def fix_empty_slugs(apps, schema_editor):
    """Generate slugs for categories with empty slugs."""
    Categoria = apps.get_model('biblioteca_ia', 'Categoria')

    for categoria in Categoria.objects.all():
        if not categoria.slug or not categoria.slug.strip():
            # Generate slug from name if available, otherwise use ID
            if categoria.nome:
                categoria.slug = slugify(categoria.nome)
            else:
                categoria.slug = f"categoria-{categoria.pk}"
            categoria.save()


def reverse_fix_empty_slugs(apps, schema_editor):
    """Reverse migration - nothing to revert."""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_ia', '0002_prompt_como_usar_prompt_exemplo_resultado_and_more'),
    ]

    operations = [
        migrations.RunPython(fix_empty_slugs, reverse_fix_empty_slugs),
    ]
