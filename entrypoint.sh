#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting Django application..."

# Wait for database to be ready (se usar PostgreSQL)
echo "⏳ Waiting for database..."
until python manage.py check --database default; do
  echo "Database is unavailable - sleeping"
  sleep 1
done
echo "✅ Database is ready!"

# Run migrations
echo "🔄 Running migrations..."
python manage.py migrate --noinput

# Create superuser if it doesn't exist
echo "👤 Creating superuser if needed..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@lpcoutinho.top', 'admin123')
    print("Superuser created: admin/admin123")
else:
    print("Superuser already exists")
EOF

# Load initial data
echo "📊 Loading initial blog posts..."
python manage.py loaddata initial_posts || echo "Initial data already loaded or not found"

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "🎉 Setup completed! Starting server..."

# Execute the main command
exec "$@"