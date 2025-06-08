#!/bin/bash

echo "🐳 Building Docker image..."

# Build da imagem
docker build -t lpcoutinho-web:latest .

echo "✅ Build completed!"

echo "🧪 Testing the container..."

# Teste rápido do container
docker run --rm -p 8000:8000 -e DJANGO_SETTINGS_MODULE=config.settings.prod lpcoutinho-web:latest &

# Aguarda o container iniciar
sleep 10

# Testa se a aplicação está respondendo
if curl -f http://localhost:8000/ > /dev/null 2>&1; then
    echo "✅ Container is working!"
else
    echo "❌ Container test failed!"
fi

# Para o container de teste
docker kill $(docker ps -q --filter ancestor=lpcoutinho-web:latest) 2>/dev/null || true

echo "🎉 Ready for deployment!"