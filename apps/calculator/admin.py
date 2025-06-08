from django.contrib import admin
from .models import CalculatorResult

@admin.register(CalculatorResult)
class CalculatorResultAdmin(admin.ModelAdmin):
    list_display = [
        'created_at', 'clt_salario_bruto', 'pj_salario_bruto', 
        'clt_liquido_mensal', 'pj_liquido_mensal', 'diferenca_mensal'
    ]
    list_filter = ['created_at']
    search_fields = ['clt_salario_bruto', 'pj_salario_bruto']
    readonly_fields = [
        'clt_liquido_mensal', 'clt_liquido_anual', 
        'pj_liquido_mensal', 'pj_liquido_anual', 
        'diferenca_mensal', 'diferenca_anual'
    ]
    
    fieldsets = (
        ('Dados CLT', {
            'fields': (
                'clt_salario_bruto', 'clt_vale_alimentacao', 'clt_vale_transporte',
                'clt_plano_saude', 'clt_outros_beneficios', 'clt_plr', 'clt_dependentes'
            )
        }),
        ('Dados PJ', {
            'fields': (
                'pj_salario_bruto', 'pj_contador', 'pj_inss', 'pj_taxa_imposto', 'pj_outros_gastos'
            )
        }),
        ('Resultados', {
            'fields': (
                'clt_liquido_mensal', 'clt_liquido_anual',
                'pj_liquido_mensal', 'pj_liquido_anual',
                'diferenca_mensal', 'diferenca_anual'
            ),
            'classes': ('collapse',)
        }),
    )
