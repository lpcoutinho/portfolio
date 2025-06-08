FROM python:3.12.3-slim

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    git \
    curl \
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

# Cria usuário não-root
RUN adduser --disabled-password --gecos '' appuser

# Por enquanto, rode como root para evitar problemas de permissão
# USER appuser

EXPOSE 8000

# Usa entrypoint para configuração inicial
ENTRYPOINT ["/entrypoint.sh"]

# Comando padrão para produção
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"]