# 🚀 Meu Portfólio Django

Portfólio profissional desenvolvido com Django e TailwindCSS, criado para demonstrar habilidades técnicas em desenvolvimento web full-stack.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de:

- **Demonstrar competências técnicas** em Django, Python e desenvolvimento web
- **Apresentar uma arquitetura profissional** e escalável de projetos Django
- **Mostrar conhecimentos em frontend moderno** utilizando TailwindCSS
- **Impressionar potenciais empregadores** e recrutadores com código de qualidade
- **Servir como base** para futuros projetos profissionais

## 🏗️ Arquitetura do Projeto

```
meu_portfolio/
├── config/                 # Configurações do projeto
│   ├── settings/
│   │   ├── base.py        # Configurações base
│   │   ├── dev.py         # Configurações de desenvolvimento
│   │   └── prod.py        # Configurações de produção
│   ├── urls.py
│   └── wsgi.py
├── apps/                   # Aplicações do projeto
│   ├── core/              # App principal (home, navegação)
│   ├── blog/              # Blog técnico
│   ├── calculator/        # Calculadora demonstrativa
│   ├── n8n_sharing/       # Compartilhamento de workflows N8N
│   └── users/             # Gestão de usuários
├── static/                # Arquivos estáticos
│   ├── js/
│   └── img/
├── templates/             # Templates HTML
│   ├── base.html         # Template base
│   └── components/       # Componentes reutilizáveis
├── media/                # Arquivos de mídia (uploads)
├── manage.py
├── requirements.txt
└── README.md
```

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.10+**
- **Django 5.2.2** - Framework web principal
- **SQLite** - Banco de dados (desenvolvimento)
- **PostgreSQL** - Banco de dados (produção)

### Frontend
- **TailwindCSS** - Framework CSS utilitário
- **HTML5 Semântico**
- **JavaScript Vanilla** - Interatividade básica

### Infraestrutura
- **Gunicorn** - WSGI Server (produção)
- **WhiteNoise** - Servir arquivos estáticos
- **Git** - Controle de versão

## 🚀 Como Executar

### Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Instalação

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd meu_portfolio
```

2. **Crie e ative um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute as migrações**
```bash
python manage.py migrate
```

5. **Crie um superusuário (opcional)**
```bash
python manage.py createsuperuser
```

6. **Execute o servidor de desenvolvimento**
```bash
python manage.py runserver
```

7. **Acesse o projeto**
   - Abra seu navegador em: http://127.0.0.1:8000/

## 📁 Funcionalidades Planejadas

### ✅ Implementado
- [x] Estrutura base do projeto Django
- [x] Configurações separadas para dev/prod
- [x] Template base responsivo com TailwindCSS
- [x] Navegação móvel funcional
- [x] Página inicial (home)

### 🔄 Em Desenvolvimento
- [ ] Sistema de blog com posts técnicos
- [ ] Calculadora interativa
- [ ] Área de compartilhamento de workflows N8N
- [ ] Sistema de autenticação de usuários
- [ ] Dashboard administrativo
- [ ] SEO otimizado
- [ ] Integração com banco PostgreSQL

### 🎯 Futuras Implementações
- [ ] API REST com Django REST Framework
- [ ] Testes automatizados (pytest)
- [ ] CI/CD com GitHub Actions
- [ ] Deploy automatizado
- [ ] Monitoramento e logs
- [ ] Cache com Redis
- [ ] CDN para assets estáticos

## 🔧 Comandos Úteis

```bash
# Executar servidor de desenvolvimento
python manage.py runserver

# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Coletar arquivos estáticos (produção)
python manage.py collectstatic

# Acessar shell Django
python manage.py shell

# Verificar problemas no projeto
python manage.py check
```

## 📝 Configuração de Ambiente

### Desenvolvimento
O projeto está configurado para usar `config.settings.dev` por padrão. Certifique-se de que:
- `DEBUG = True`
- Banco SQLite local
- Logs detalhados habilitados

### Produção
Para produção, configure as variáveis de ambiente:
```bash
export DJANGO_SETTINGS_MODULE=config.settings.prod
export SECRET_KEY=sua_secret_key_super_secreta
export DB_NAME=nome_do_banco
export DB_USER=usuario_do_banco
export DB_PASSWORD=senha_do_banco
export DB_HOST=host_do_banco
export ALLOWED_HOSTS=seudominio.com,www.seudominio.com
```

## 🤝 Contribuição

Este é um projeto de portfólio pessoal, mas sugestões são sempre bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add: Amazing Feature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Contato

- **LinkedIn**: [Seu LinkedIn]
- **GitHub**: [Seu GitHub]
- **Email**: seu.email@exemplo.com

---

**💡 Este projeto foi desenvolvido como demonstração de habilidades técnicas em Django e desenvolvimento web moderno.**