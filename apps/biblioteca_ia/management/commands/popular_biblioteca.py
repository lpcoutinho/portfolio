from django.core.management.base import BaseCommand
from apps.biblioteca_ia.models import Categoria, Prompt


class Command(BaseCommand):
    help = 'Popula a biblioteca de IA com categorias e prompts iniciais'

    def handle(self, *args, **options):
        # Dados das categorias
        categorias_data = [
            {
                'nome': 'Imagens Ultra Realistas',
                'icone': '📸',
                'descricao': 'Prompts para criar fotos e imagens com qualidade profissional',
                'ordem': 1,
                'prompts': [
                    {
                        'titulo': '👩 Influenciadora Digital',
                        'conteudo': 'Create a hyperrealistic photo of a young Brazilian female influencer, 25 years old, holding a product in her right hand, smiling naturally, shot with iPhone 15 Pro, shallow depth of field, warm lifestyle lighting, white minimalist background, magazine quality.',
                        'descricao_curta': 'Foto hiper-realista de influenciadora brasileira segurando produto',
                        'ordem': 1,
                    },
                    {
                        'titulo': '📦 Foto de Produto Premium',
                        'conteudo': 'Ultra realistic studio product photo: [PRODUTO] on a white marble surface, soft shadow, professional lighting from 45 degrees, crisp details, brand photography style, 8K resolution, isolated background, e-commerce ready.',
                        'descricao_curta': 'Foto de estúdio profissional de produto com iluminação perfeita',
                        'ordem': 2,
                    },
                    {
                        'titulo': '📱 Foto Estilo iPhone',
                        'conteudo': 'iPhone 15 Pro Max photo quality, candid lifestyle shot, 28mm focal length, natural skin tones, slight lens blur background, golden hour lighting, real life authentic feel, no filters, shot at f/1.8, HEIF file quality.',
                        'descricao_curta': 'Foto estilo iPhone com qualidade de câmera profissional',
                        'ordem': 3,
                    },
                    {
                        'titulo': '🌟 Lifestyle Aspiracional',
                        'conteudo': 'Photorealistic lifestyle scene: affluent young adult in a bright modern apartment, using a laptop, coffee on the table, natural window light, cozy productive atmosphere, aspirational digital nomad aesthetic, warm tones.',
                        'descricao_curta': 'Cena lifestyle de jovem em apartamento moderno trabalhando',
                        'ordem': 4,
                    },
                    {
                        'titulo': '🤖 Avatar de IA Feminino',
                        'conteudo': 'Hyperrealistic AI influencer female, 24 years old, Brazilian features, confident smile, professional studio lighting, sharp eyes, clean skin, neutral makeup, suitable for brand ambassador, neutral background, photorealistic render.',
                        'descricao_curta': 'Avatar de IA feminina com características brasileiras',
                        'ordem': 5,
                    },
                    {
                        'titulo': '✨ Foto de Antes e Depois',
                        'conteudo': 'Split screen before and after transformation photo, left side: dull tired skin, right side: glowing healthy skin, same lighting, same angle, realistic skin texture, professional beauty photography, no makeup left vs full glow right.',
                        'descricao_curta': 'Foto antes e depois mostrando transformação de pele',
                        'ordem': 6,
                    },
                    {
                        'titulo': '💻 Mockup de Produto Digital',
                        'conteudo': 'Photorealistic device mockup, MacBook Pro screen displaying a digital product cover, professional desk setup, soft lighting, shallow depth of field, clean workspace aesthetic, blurred background, product showcase style.',
                        'descricao_curta': 'Mockup profissional de produto digital em MacBook',
                        'ordem': 7,
                    },
                    {
                        'titulo': '🛒 Foto TikTok Shop',
                        'conteudo': 'TikTok Shop product photo style, vibrant colors, young trendy aesthetic, product in use by diverse person, candid feel, bright lighting, millennial pink or Gen Z blue background, engaging visual composition.',
                        'descricao_curta': 'Foto estilo TikTok Shop com cores vibrantes e jovens',
                        'ordem': 8,
                    },
                    {
                        'titulo': '📚 Capa de Ebook Premium',
                        'conteudo': 'Professional ebook cover design, title: [TITULO], modern minimalist design, gradient background from deep blue to purple, bold typography, AI theme, clean layout, best seller book cover style, high contrast, premium feel.',
                        'descricao_curta': 'Capa de ebook profissional com design moderno',
                        'ordem': 9,
                    },
                    {
                        'titulo': '🎥 Background para Webinar',
                        'conteudo': 'Professional virtual background for video call, modern home office setup, bookshelves, soft ambient lighting, clean aesthetic, brand colors (blue and white), no clutter, HD quality, ideal for professional Zoom or YouTube live.',
                        'descricao_curta': 'Background virtual profissional para videochamadas',
                        'ordem': 10,
                    },
                    {
                        'titulo': '📣 Imagem para Anúncio Meta',
                        'conteudo': 'High conversion Facebook ad image, bold text overlay space at top, product featured prominently, bright contrasting colors, human face with expression of surprise or joy, white border, square format 1:1, professional advertising quality.',
                        'descricao_curta': 'Imagem de anúncio com alta taxa de conversão',
                        'ordem': 11,
                    },
                    {
                        'titulo': '💬 Foto de Depoimento',
                        'conteudo': 'Realistic testimonial photo, happy customer smiling holding a product or smartphone, candid authentic feel, home or cafe background, natural lighting, trust and satisfaction expression, relatable everyday person look.',
                        'descricao_curta': 'Foto autêntica de cliente satisfeito com depoimento',
                        'ordem': 12,
                    },
                ]
            },
            {
                'nome': 'Vídeos com IA',
                'icone': '🎬',
                'descricao': 'Crie vídeos impressionantes usando inteligência artificial',
                'ordem': 2,
                'prompts': []
            },
            {
                'nome': 'TikTok Shop',
                'icone': '🛍️',
                'descricao': 'Prompts otimizados para vendas no TikTok Shop',
                'ordem': 3,
                'prompts': []
            },
            {
                'nome': 'Negócios Digitais',
                'icone': '💼',
                'descricao': 'Estratégias e prompts para empreender digitalmente',
                'ordem': 4,
                'prompts': []
            },
            {
                'nome': 'Renda Extra',
                'icone': '💰',
                'descricao': 'Prompts para gerar renda adicional com IA',
                'ordem': 5,
                'prompts': []
            },
            {
                'nome': 'Marketing Digital',
                'icone': '📊',
                'descricao': 'Prompts para estratégias de marketing e vendas',
                'ordem': 6,
                'prompts': []
            },
            {
                'nome': 'Conteúdo Viral',
                'icone': '🔥',
                'descricao': 'Crie conteúdo com potencial viral',
                'ordem': 7,
                'prompts': []
            },
            {
                'nome': 'Automação',
                'icone': '⚡',
                'descricao': 'Automatize processos com inteligência artificial',
                'ordem': 8,
                'prompts': []
            },
            {
                'nome': 'Iniciantes',
                'icone': '🎓',
                'descricao': 'Prompts ideais para quem está começando com IA',
                'ordem': 9,
                'prompts': []
            },
            {
                'nome': 'Avançados',
                'icone': '🚀',
                'descricao': 'Prompts complexos para usuários experientes',
                'ordem': 10,
                'prompts': []
            },
        ]

        # Criar categorias e prompts
        total_criados = 0
        total_prompts = 0

        for cat_data in categorias_data:
            # Verificar se categoria já existe
            categoria, created = Categoria.objects.get_or_create(
                slug=cat_data['nome'].lower().replace(' ', '-').replace('á', 'a').replace('ê', 'e').replace('ã', 'a'),
                defaults={
                    'nome': cat_data['nome'],
                    'icone': cat_data['icone'],
                    'descricao': cat_data['descricao'],
                    'ordem': cat_data['ordem'],
                }
            )

            if created:
                total_criados += 1
                self.stdout.write(self.style.SUCCESS(f'Categoria criada: {categoria.nome}'))
            else:
                self.stdout.write(self.style.WARNING(f'Categoria já existe: {categoria.nome}'))

            # Criar prompts da categoria
            for prompt_data in cat_data['prompts']:
                prompt, p_created = Prompt.objects.get_or_create(
                    titulo=prompt_data['titulo'],
                    categoria=categoria,
                    defaults={
                        'conteudo': prompt_data['conteudo'],
                        'descricao_curta': prompt_data.get('descricao_curta', ''),
                        'ordem': prompt_data.get('ordem', 0),
                    }
                )

                if p_created:
                    total_prompts += 1
                    self.stdout.write(self.style.SUCCESS(f'  Prompt criado: {prompt.titulo}'))
                else:
                    self.stdout.write(self.style.WARNING(f'  Prompt já existe: {prompt.titulo}'))

        self.stdout.write(self.style.SUCCESS(f'\nTotal: {total_criados} categorias e {total_prompts} prompts criados!'))
        self.stdout.write(self.style.SUCCESS(f'\nAcesse: http://localhost:8000/biblioteca-ia/'))
