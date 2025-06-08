#!/bin/bash

echo "🔄 Rebuilding and updating LP Coutinho..."

# Rebuild da imagem
echo "🐳 Building new Docker image..."
docker build -t lpcoutinho-web:latest .

# Atualizar serviço no swarm
echo "🚀 Updating Docker Swarm service..."
docker service update --force --image lpcoutinho-web:latest lpcoutinho_lpcoutinho-web

# Aguardar o serviço ficar pronto
echo "⏳ Waiting for service to be ready..."
sleep 30

# Verificar status
echo "✅ Service status:"
docker service ps lpcoutinho_lpcoutinho-web --no-trunc

echo "📋 Service logs (last 50 lines):"
docker service logs lpcoutinho_lpcoutinho-web --tail 50

echo "🎉 Update completed!"