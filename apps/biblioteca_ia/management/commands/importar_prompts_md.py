from django.core.management.base import BaseCommand
from apps.biblioteca_ia.models import Categoria, Prompt
import os


class Command(BaseCommand):
    help = 'Importa os 120 prompts do arquivo prompts.md'

    def handle(self, *args, **options):
        # Mapeamento de categorias
        categoria_icone_map = {
            'Imagens Ultra Realistas': '📸',
            'Vídeos com IA': '🎬',
            'TikTok Shop': '🛍️',
            'Negócios Digitais': '💼',
            'Renda Extra': '💰',
            'Marketing Digital': '📊',
            'Conteúdo Viral': '🔥',
            'Automação': '⚡',
            'Iniciantes': '🎓',
            'Avançados': '🚀',
        }

        # Ler o arquivo
        caminho_arquivo = '/home/lpcoutinho/projects/portfolio/prompts.md'

        if not os.path.exists(caminho_arquivo):
            self.stdout.write(self.style.ERROR(f'Arquivo não encontrado: {caminho_arquivo}'))
            return

        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        # Processar o arquivo
        prompts_importados = 0
        i = 0
        total_linhas = len(linhas)

        while i < total_linhas:
            linha = linhas[i].strip()

            # Verificar se é o início de um novo prompt (número)
            if linha.isdigit():
                numero = int(linha)

                # Ler título (próxima linha)
                if i + 1 < total_linhas:
                    titulo = linhas[i + 1].strip()

                    # Ler categoria (próxima linha)
                    if i + 2 < total_linhas:
                        nome_categoria = linhas[i + 2].strip()

                        # Ler conteúdo do prompt (próxima linha)
                        if i + 3 < total_linhas:
                            conteudo = linhas[i + 3].strip()

                            # Pular linhas vazias
                            i += 4
                            while i < total_linhas and not linhas[i].strip():
                                i += 1

                            # Ler "Para que serve"
                            para_que_serve = ""
                            if i < total_linhas and "Para que serve" in linhas[i]:
                                i += 1
                                while i < total_linhas and linhas[i].strip() and not "Como usar" in linhas[i]:
                                    para_que_serve += linhas[i].strip() + " "
                                    i += 1

                            # Pular até "Como usar"
                            while i < total_linhas and "Como usar" not in linhas[i]:
                                i += 1

                            # Ler "Como usar"
                            como_usar = ""
                            if i < total_linhas and "Como usar" in linhas[i]:
                                i += 1
                                while i < total_linhas and linhas[i].strip() and not "Resultado esperado" in linhas[i]:
                                    como_usar += linhas[i].strip() + " "
                                    i += 1

                            # Pular até "Resultado esperado"
                            while i < total_linhas and "Resultado esperado" not in linhas[i]:
                                i += 1

                            # Ler "Resultado esperado"
                            resultado_esperado = ""
                            if i < total_linhas and "Resultado esperado" in linhas[i]:
                                i += 1
                                while i < total_linhas and linhas[i].strip() and not "Exemplo de resultado" in linhas[i]:
                                    resultado_esperado += linhas[i].strip() + " "
                                    i += 1

                            # Pular até "Exemplo de resultado"
                            while i < total_linhas and "Exemplo de resultado" not in linhas[i]:
                                i += 1

                            # Ler "Exemplo de resultado"
                            exemplo_resultado = ""
                            if i < total_linhas and "Exemplo de resultado" in linhas[i]:
                                i += 1
                                while i < total_linhas and linhas[i].strip() and not linhas[i].strip().isdigit():
                                    exemplo_resultado += linhas[i].strip() + " "
                                    i += 1

                            # Criar ou obter categoria
                            categoria, created = Categoria.objects.get_or_create(
                                slug=nome_categoria.lower().replace(' ', '-').replace('á', 'a').replace('ê', 'e').replace('ã', 'a').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ç', 'c'),
                                defaults={
                                    'nome': nome_categoria,
                                    'icone': categoria_icone_map.get(nome_categoria, '📝'),
                                    'descricao': f'Prompts de {nome_categoria}',
                                    'ordem': list(categoria_icone_map.keys()).index(nome_categoria) + 1 if nome_categoria in categoria_icone_map else 99,
                                }
                            )

                            if created:
                                self.stdout.write(self.style.SUCCESS(f'✓ Categoria criada: {categoria.nome}'))

                            # Criar descrição curta (apenas para preview)
                            descricao_curta = para_que_serve.strip()
                            # Limitar a 300 caracteres
                            if len(descricao_curta) > 280:
                                descricao_curta = descricao_curta[:280] + "..."

                            # Criar ou atualizar prompt com campos separados
                            prompt, p_created = Prompt.objects.get_or_create(
                                titulo=titulo,
                                categoria=categoria,
                                defaults={
                                    'conteudo': conteudo,
                                    'descricao_curta': descricao_curta,
                                    'para_que_serve': para_que_serve.strip(),
                                    'como_usar': como_usar.strip(),
                                    'resultado_esperado': resultado_esperado.strip(),
                                    'exemplo_resultado': exemplo_resultado.strip(),
                                    'ordem': numero,
                                }
                            )

                            if p_created:
                                prompts_importados += 1
                                self.stdout.write(self.style.SUCCESS(f'  ✓ Prompt #{numero}: {titulo}'))
                            else:
                                # Atualizar se já existe
                                prompt.conteudo = conteudo
                                prompt.descricao_curta = descricao_curta
                                prompt.para_que_serve = para_que_serve.strip()
                                prompt.como_usar = como_usar.strip()
                                prompt.resultado_esperado = resultado_esperado.strip()
                                prompt.exemplo_resultado = exemplo_resultado.strip()
                                prompt.ordem = numero
                                prompt.save()
                                self.stdout.write(self.style.WARNING(f'  ⚠ Prompt atualizado #{numero}: {titulo}'))

                            # Pular linhas vazias até o próximo prompt
                            while i < total_linhas and (not linhas[i].strip() or not linhas[i].strip().isdigit()):
                                i += 1
                            continue

            i += 1

        self.stdout.write(self.style.SUCCESS(f'\n🎉 Importação concluída!'))
        self.stdout.write(self.style.SUCCESS(f'Total de prompts importados: {prompts_importados}'))

        # Mostrar resumo por categoria
        self.stdout.write(self.style.SUCCESS(f'\n📊 Resumo por categoria:'))
        for categoria in Categoria.objects.all():
            total = categoria.prompts.count()
            self.stdout.write(f'  {categoria.icone} {categoria.nome}: {total} prompts')
