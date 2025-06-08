from django.db import models
from django.utils import timezone
import json

class AnalyticsEvent(models.Model):
    """
    Modelo para armazenar eventos de analytics customizados.
    """
    EVENT_TYPES = [
        ('page_load', 'Page Load'),
        ('contact_click', 'Contact Click'),
        ('scroll_depth', 'Scroll Depth'),
        ('time_on_page', 'Time on Page'),
        ('external_link', 'External Link'),
        ('file_download', 'File Download'),
    ]
    
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    timestamp = models.DateTimeField(default=timezone.now)
    
    # Dados do usuário
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    referrer = models.URLField(blank=True)
    page_url = models.URLField()
    
    # Dados técnicos
    language = models.CharField(max_length=10, blank=True)
    screen_resolution = models.CharField(max_length=20, blank=True)
    viewport_size = models.CharField(max_length=20, blank=True)
    timezone_info = models.CharField(max_length=50, blank=True)
    
    # Dados customizados (JSON)
    custom_data = models.JSONField(default=dict, blank=True)
    
    # Dados de sessão
    session_id = models.CharField(max_length=40, blank=True)
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['event_type', 'timestamp']),
            models.Index(fields=['ip_address', 'timestamp']),
            models.Index(fields=['page_url']),
        ]
    
    def __str__(self):
        return f"{self.event_type} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

class VisitorSession(models.Model):
    """
    Modelo para agrupar eventos por sessão de visitante.
    """
    session_id = models.CharField(max_length=40, unique=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    
    # Primeira e última atividade
    first_seen = models.DateTimeField(default=timezone.now)
    last_seen = models.DateTimeField(default=timezone.now)
    
    # Contadores
    page_views = models.PositiveIntegerField(default=0)
    total_time_seconds = models.PositiveIntegerField(default=0)
    
    # Dados geográficos (se disponível)
    country = models.CharField(max_length=2, blank=True)
    city = models.CharField(max_length=100, blank=True)
    
    class Meta:
        ordering = ['-last_seen']
    
    def __str__(self):
        return f"Session {self.session_id[:8]} - {self.ip_address}"

class PageView(models.Model):
    """
    Modelo para contabilizar visualizações de página.
    """
    page_url = models.URLField()
    timestamp = models.DateTimeField(default=timezone.now)
    session = models.ForeignKey(VisitorSession, on_delete=models.CASCADE, related_name='pageviews')
    
    # Dados da página
    page_title = models.CharField(max_length=200, blank=True)
    referrer = models.URLField(blank=True)
    
    # Métricas de engajamento
    time_on_page = models.PositiveIntegerField(default=0)  # em segundos
    scroll_depth = models.PositiveIntegerField(default=0)  # percentual
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['page_url', 'timestamp']),
            models.Index(fields=['session', 'timestamp']),
        ]
    
    def __str__(self):
        return f"{self.page_url} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
