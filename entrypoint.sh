#!/bin/bash

# Exit on any error
set -e

# Trap para capturar erros e mostrar informações úteis
trap 'echo "❌ ERROR: Script failed at line $LINENO. Exit code: $?"' ERR

echo "🚀 Starting Django application..."
echo "📋 Environment info:"
echo "   - PYTHONUNBUFFERED: $PYTHONUNBUFFERED"
echo "   - DJANGO_SETTINGS_MODULE: $DJANGO_SETTINGS_MODULE"
echo "   - DEBUG: $DEBUG"

# Ensure directories exist with correct permissions
echo "📁 Setting up data directory..."
mkdir -p /app/data /app/logs /app/staticfiles /app/media
chmod 755 /app/data /app/logs /app/staticfiles /app/media

# Verificar permissões nos diretórios de volumes
echo "🔒 Checking volume permissions..."
ls -la /app/data /app/logs /app/staticfiles /app/media 2>/dev/null || echo "Some directories may not exist yet"

# Check if database file exists, if not create it
if [ ! -f "/app/data/db.sqlite3" ]; then
    echo "📊 Creating new database file..."
    touch /app/data/db.sqlite3
    chmod 644 /app/data/db.sqlite3
    echo "✅ Database file created"
else
    echo "✅ Database file already exists"
fi

# Check database permissions
echo "🔒 Checking database permissions..."
ls -la /app/data/db.sqlite3

# Run Django system check
echo "🔍 Running Django system check..."
python manage.py check --deploy || echo "⚠️  Some deployment warnings detected"

# Run migrations
echo "🔄 Running migrations..."
python manage.py migrate --noinput || echo "⚠️  Migrations may have issues"

# Create superuser if it doesn't exist
echo "👤 Creating superuser if needed..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@lpcoutinho.top', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
" || echo "⚠️  Superuser creation skipped"

# Load initial data
echo "📚 Loading initial blog posts..."
python manage.py loaddata initial_posts 2>/dev/null || echo "ℹ️  Initial data already loaded or not found"

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput || echo "⚠️  Static collection may have issues"

# Test if Gunicorn is available
echo "🧪 Checking Gunicorn installation..."
if command -v gunicorn &> /dev/null; then
    echo "✅ Gunicorn found: $(gunicorn --version)"
else
    echo "❌ Gunicorn not found, trying to install..."
    pip install gunicorn
fi

# Test basic Django response before starting server
echo "🧪 Testing Django response..."
python manage.py shell -c "
from django.test import Client
client = Client()
try:
    response = client.get('/')
    print(f'✅ Django test response: {response.status_code}')
except Exception as e:
    print(f'⚠️  Django test failed: {e}')
" || echo "⚠️  Django test failed"

echo "🎉 Setup completed! Starting server on 0.0.0.0:8000..."

# Execute the main command
exec "$@"