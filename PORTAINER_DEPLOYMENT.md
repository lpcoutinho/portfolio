# Instruções para Deploy no Portainer

## Problema Identificado
O erro HTTP 504 Gateway Timeout ocorre quando o Traefik não consegue conectar ao seu container Django.

## Correções Aplicadas

### 1. **Dockerfile** (`/root/portfolio/Dockerfile`)
- ✅ Garantiu instalação do `curl` e `ca-certificates` para healthcheck
- ✅ Adicionou healthcheck nativo no Dockerfile
- ✅ Otimizou configuração do Gunicorn (2 workers + 4 threads)
- ✅ Adicionou logging de acesso e erro do Gunicorn

### 2. **Entrypoint** (`/root/portfolio/entrypoint.sh`)
- ✅ Adicionou captura de erros com mensagens detalhadas
- ✅ Adicionou verificação de permissões nos volumes
- ✅ Adicionou teste de resposta do Django antes de iniciar o servidor
- ✅ Adicionou verificação do Gunicorn antes do startup

### 3. **Configurações de Produção** (`config/settings/prod.py`)
- ✅ Ativou cookies seguros (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE)
- ✅ Adicionou configurações HSTS para segurança HTTPS
- ✅ Ativou HTTP-only cookies para segurança

### 4. **Docker Compose** (`docker-compose.yml`)
- ✅ Corrigiu erro de sintaxe no redirect www (era `$${1}`, agora `${1}`)
- ✅ Adicionou `container_name` para facilitar debugging
- ✅ Aumentou `start_period` do healthcheck de 60s para 90s
- ✅ Adicionado variável de ambiente `DEBUG=0` para evitar inconsistências
- ✅ Melhorada configuração de headers do Traefik

## Passos para Deploy no Portainer

### Passo 1: Build da Nova Imagem

No terminal do seu servidor:

```bash
cd /root/portfolio
docker build -t lpcoutinho-web:latest .
```

### Passo 2: Atualizar Stack no Portainer

1. Acesse o Portainer
2. Vá em **Stacks** → Selecione seu stack `lpcoutinho-web`
3. **Importante**: Copie o conteúdo atualizado do arquivo `docker-compose.yml`
4. Substitua o conteúdo do editor do Portainer
5. Clique em **"Update the stack"**

### Passo 3: Verificar Logs

No Portainer:
1. Vá em **Containers** → `lpcoutinho-web`
2. Clique em **Logs** para ver o startup do container
3. Procure por mensagens de erro ou avisos

### Passo 4: Testar a Aplicação

```bash
# Testar localmente no servidor
curl -v http://localhost:8000/

# Testar via HTTPS externo
curl -v https://lpcoutinho.top/
```

## Troubleshooting

### Se continuar com erro 504:

1. **Verificar logs detalhados:**
   ```bash
   docker logs lpcoutinho-web -f
   ```

2. **Verificar se o container está rodando:**
   ```bash
   docker ps | grep lpcoutinho-web
   ```

3. **Verificar healthcheck:**
   ```bash
   docker inspect lpcoutinho-web --format='{{.State.Health.Status}}'
   ```

4. **Testar conexão direta ao container:**
   ```bash
   docker exec -it lpcoutinho-web curl -v http://localhost:8000/
   ```

5. **Verificar permissões nos volumes:**
   ```bash
   docker exec -it lpcoutinho-web ls -la /app/data/
   ```

### Se houver erro de permissão nos volumes:

```bash
# Corrigir permissões dos volumes
docker exec -it lpcoutinho-web chown -R appuser:appuser /app/data /app/logs /app/staticfiles /app/media
docker exec -it lpcoutinho-web chmod -R 755 /app/data /app/logs /app/staticfiles /app/media
```

### Se houver erro de database:

```bash
# Acessar o container e verificar database
docker exec -it lpcoutinho-web python manage.py migrate
docker exec -it lpcoutinho-web python manage.py check
```

## Informações de Acesso

- **Admin URL**: https://lpcoutinho.top/admin/
- **Admin User**: admin
- **Admin Password**: admin123

**Importante**: Altere a senha do admin após o primeiro acesso!

## Variáveis de Ambiente Opcionais

Você pode definir estas variáveis no Portainer:

```yaml
environment:
  - SECRET_KEY=your-very-secret-key-here
  - DEBUG=0
  - DJANGO_SETTINGS_MODULE=config.settings.prod
```

## Monitoramento

Após o deploy, monitore:
- Status do container no Portainer
- Health status (deve ser "healthy")
- Logs do container
- Resposta do site no navegador
