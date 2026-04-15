from django.core.management.base import BaseCommand
from apps.biblioteca_ia.models import Prompt
from django.core.files import File
import os


class Command(BaseCommand):
    help = 'Associa imagens do diretório static/ aos prompts correspondentes'

    def handle(self, *args, **options):
        # Mapeamento de nome de arquivo para título do prompt (parcial)
        imagem_para_prompt = {
            'antes-e-depois.png': 'Foto de Antes e Depois',
            'avatar-ia-feminio.png': 'Avatar de IA Feminino',
            'com-produto.png': 'Com produto',
            'com-roupa.png': 'Com roupa',
            'empresas.png': 'Para Empresas',
            'iphone-15-pro-max.png': 'Foto Estilo iPhone',
            'lifestyle.png': 'Lifestyle Aspiracional',
            'mockup.png': 'Mockup de Produto Digital',
            'para-anuncios.png': 'Imagem para Anúncio Meta',
            'para-vitrine.png': 'Foto de Produto Premium',
        }

        caminho_static = '/home/lpcoutinho/projects/portfolio/static'
        imagens_encontradas = 0
        prompts_atualizados = 0

        self.stdout.write('=== Associando imagens aos prompts ===\n')

        for nome_arquivo, titulo_prompt in imagem_para_prompt.items():
            caminho_completo = os.path.join(caminho_static, nome_arquivo)

            if os.path.exists(caminho_completo):
                imagens_encontradas += 1
                self.stdout.write(f'📷 {nome_arquivo}')

                # Buscar prompt correspondente
                prompts = Prompt.objects.filter(titulo__icontains=titulo_prompt)

                if prompts.exists():
                    for prompt in prompts:
                        # Abrir o arquivo e associar ao prompt
                        with open(caminho_completo, 'rb') as f:
                            prompt.imagem.save(nome_arquivo, File(f), save=True)
                            prompts_atualizados += 1
                            self.stdout.write(self.style.SUCCESS(f'  ✓ Associado a: {prompt.titulo}'))
                else:
                    self.stdout.write(self.style.WARNING(f'  ⚠ Nenhum prompt encontrado para: {titulo_prompt}'))
            else:
                self.stdout.write(self.style.ERROR(f'  ❌ Arquivo não encontrado: {nome_arquivo}'))

        self.stdout.write(f'\n🎉 Processo concluído!')
        self.stdout.write(f'Imagens encontradas: {imagens_encontradas}')
        self.stdout.write(self.style.SUCCESS(f'Prompts atualizados: {prompts_atualizados}'))
