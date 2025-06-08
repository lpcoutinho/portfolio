# Deploy Guide - LP Coutinho

## 🚀 Processo de Deploy

### 1. Configuração no Servidor (VPS)

```bash
# Clone do repositório
cd ~
git clone https://github.com/seu-usuario/portfolio.git
cd portfolio

# Criar volumes no Docker Swarm
docker volume create lpcoutinho-data
docker volume create lpcoutinho-static
docker volume create lpcoutinho-media
docker volume create lpcoutinho-logs

# Primeira build da imagem
docker build -t lpcoutinho-web:latest .
```

### 2. Configuração no Portainer

1. **Criar Stack no Portainer:**
   - Nome: `lpcoutinho`
   - Copiar conteúdo do `docker-compose.yml`

2. **Variáveis de Ambiente:**
   - `SECRET_KEY`: Gerar uma chave secreta Django
   - `DJANGO_SETTINGS_MODULE`: `config.settings.prod`

3. **Volumes Externos:**
   - `lpcoutinho-static`: Para arquivos estáticos
   - `lpcoutinho-media`: Para uploads de mídia

### 3. Configuração GitHub Actions

**Secrets necessários no GitHub:**
- `SERVER_IP`: IP do seu servidor VPS
- `SERVER_USER`: Usuário SSH (geralmente root)
- `SERVER_SSH_KEY`: Chave privada SSH

### 4. Configuração Traefik

O docker-compose já inclui labels para:
- SSL automático via Let's Encrypt
- Redirect www → não-www
- Proxy reverso

### 5. Deploy Automático

1. **Push para main:**
   ```bash
   git add .
   git commit -m "Deploy to production"
   git push origin main
   ```

2. **Deploy manual:**
   - GitHub Actions → Actions → Deploy to Production → Run workflow

## 🔧 Comandos Úteis

### Logs
```bash
# Ver logs do serviço
docker service logs lpcoutinho_lpcoutinho-web -f

# Logs do container
docker logs container_id -f
```

### Manutenção
```bash
# Atualizar serviço
docker service update --force lpcoutinho_lpcoutinho-web

# Escalar serviço
docker service scale lpcoutinho_lpcoutinho-web=2

# Entrar no container
docker exec -it container_id bash
```

### Django Management
```bash
# Executar comandos Django no container
docker exec -it container_id python manage.py shell
docker exec -it container_id python manage.py createsuperuser
docker exec -it container_id python manage.py migrate
```

## 🔒 Segurança

### Configurações Importantes:
1. **SECRET_KEY**: Gerar chave única para produção
2. **ALLOWED_HOSTS**: Configurado para seu domínio
3. **SSL**: Configurado via Traefik + Let's Encrypt
4. **Database**: SQLite inicialmente (migrar para PostgreSQL se necessário)

### Gerar SECRET_KEY:
```python
import secrets
print(secrets.token_urlsafe(50))
```

## 📊 Monitoramento

### Health Check
```bash
# Verificar se aplicação está rodando
curl -I https://lpcoutinho.top/

# Ver status dos serviços
docker service ls
```

### Backup
```bash
# Backup do banco SQLite
docker cp container_id:/app/db.sqlite3 ./backup-$(date +%Y%m%d).sqlite3

# Backup dos volumes
docker run --rm -v lpcoutinho-static:/source -v /backup:/backup alpine tar czf /backup/static-backup.tar.gz -C /source .
```

## 🐛 Troubleshooting

### Problemas Comuns:

1. **Serviço não inicia:**
   ```bash
   docker service logs lpcoutinho_lpcoutinho-web
   ```

2. **Erro de migração:**
   ```bash
   docker exec -it container_id python manage.py migrate --fake-initial
   ```

3. **Arquivos estáticos não carregam:**
   ```bash
   docker exec -it container_id python manage.py collectstatic --noinput
   ```

4. **SSL não funciona:**
   - Verificar se domínio aponta para o servidor
   - Verificar logs do Traefik

## 📈 Próximos Passos

1. **Migrar para PostgreSQL:**
   - Adicionar serviço postgres no docker-compose
   - Atualizar settings de produção

2. **Redis para Cache:**
   - Adicionar serviço Redis
   - Configurar cache do Django

3. **Monitoring:**
   - Prometheus + Grafana
   - Log aggregation

4. **Backup Automático:**
   - Cron job para backup do banco
   - Backup para cloud storage