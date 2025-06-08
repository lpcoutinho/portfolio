#!/bin/bash

echo "🚀 Setting up LP Coutinho deployment environment..."

# Criar volumes Docker
echo "📦 Creating Docker volumes..."
docker volume create lpcoutinho-data
docker volume create lpcoutinho-static  
docker volume create lpcoutinho-media
docker volume create lpcoutinho-logs

# Verificar se os volumes foram criados
echo "✅ Volumes created:"
docker volume ls | grep lpcoutinho

# Build da primeira imagem
echo "🐳 Building initial Docker image..."
docker build -t lpcoutinho-web:latest .

echo "🎉 Setup completed!"
echo ""
echo "Next steps:"
echo "1. Create a stack in Portainer with the content of docker-compose.yml"
echo "2. Update the SECRET_KEY environment variable"
echo "3. Deploy the stack"
echo ""
echo "Or run the GitHub Actions deploy workflow"