# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

```bash
# Development server
python manage.py runserver

# Database operations
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Project health checks
python manage.py check
python manage.py check --deploy

# Shell access
python manage.py shell

# Static files (production)
python manage.py collectstatic
```

## Architecture Overview

This is a Django 5.2.2 portfolio project with a **modular app-based architecture** using **separated settings configuration**.

### Settings Architecture
- **Base settings**: `config/settings/base.py` - shared configuration
- **Development**: `config/settings/dev.py` - extends base, uses SQLite
- **Production**: `config/settings/prod.py` - extends base, uses PostgreSQL
- **Default environment**: Development (`config.settings.dev` in `manage.py`)

### App Structure
- **`apps/core/`** - Main app with home page and navigation
- **`apps/blog/`** - Blog functionality (placeholder URLs)
- **`apps/calculator/`** - Calculator demo (placeholder URLs)
- **`apps/n8n_sharing/`** - N8N workflow sharing (placeholder URLs)
- **`apps/users/`** - User management (placeholder URLs)

### URL Routing Pattern
- Root URLs in `config/urls.py` include app URLs with prefixes
- Each app has its own `urls.py` with `app_name` namespace
- Static/media files served in development via `settings.DEBUG` check

### Template System
- **Base template**: `templates/base.html` with TailwindCSS CDN
- **App templates**: `templates/{app_name}/` structure
- **Components**: `templates/components/` for reusable elements
- **Responsive navigation** with mobile menu toggle

### App Configuration Requirements
When creating new apps in `apps/` directory:
1. Update `apps.py` to set `name = 'apps.{app_name}'`
2. Add to `LOCAL_APPS` in `config/settings/base.py`
3. Create `urls.py` with `app_name` namespace
4. Include in `config/urls.py` with appropriate prefix

### Environment Variables (Production)
- `DJANGO_SETTINGS_MODULE=config.settings.prod`
- `SECRET_KEY` - Django secret key
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` - PostgreSQL config
- `ALLOWED_HOSTS` - comma-separated domain list

### Frontend Stack
- **TailwindCSS** via CDN in base template
- **Responsive design** with mobile-first approach
- **JavaScript** for mobile menu toggle functionality
- **Static files** in `/static/js/` and `/static/img/`

### Key Conventions
- Portuguese language (`pt-br`) and São Paulo timezone
- Apps use class-based and function-based views as appropriate
- URL names follow `app_name:view_name` pattern
- Templates extend `base.html` and use `{% block %}` structure