FROM python:3.12.3-slim

WORKDIR /app

# Instala dependências do sistema (incluindo curl para healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    git \
    curl \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Sao_Paulo
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings.prod

# Copia e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Garante que entrypoint tenha permissão de execução
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Cria diretórios para dados persistentes como root
RUN mkdir -p /app/data /app/logs /app/staticfiles /app/media
RUN chmod 777 /app/data /app/logs /app/staticfiles /app/media

# Cria usuário não-root
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app

# Por enquanto, rode como root para evitar problemas de permissão
# USER appuser

EXPOSE 8000

# Healthcheck usando curl para verificar se o servidor está respondendo
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# Usa entrypoint para configuração inicial
ENTRYPOINT ["/entrypoint.sh"]

# Comando padrão para produção (configuração otimizada)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--threads", "4", "--timeout", "120", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "info"]