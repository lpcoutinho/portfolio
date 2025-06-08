#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting Django application..."

# Ensure directories exist with correct permissions
echo "📁 Setting up data directory..."
mkdir -p /app/data /app/logs /app/staticfiles /app/media
chmod 755 /app/data /app/logs /app/staticfiles /app/media

# Check if database file exists, if not create it
if [ ! -f "/app/data/db.sqlite3" ]; then
    echo "📊 Creating new database file..."
    touch /app/data/db.sqlite3
    chmod 644 /app/data/db.sqlite3
fi

# Run Django system check
echo "🔍 Running Django system check..."
python manage.py check

# Run migrations
echo "🔄 Running migrations..."
python manage.py migrate --noinput

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
" || echo "Superuser creation skipped"

# Load initial data
echo "📚 Loading initial blog posts..."
python manage.py loaddata initial_posts || echo "Initial data already loaded or not found"

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "🎉 Setup completed! Starting server..."

# Execute the main command
exec "$@"