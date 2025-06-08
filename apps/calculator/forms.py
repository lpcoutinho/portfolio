from django import forms
from .models import CalculatorResult

class CalculatorForm(forms.ModelForm):
    class Meta:
        model = CalculatorResult
        fields = [
            # CLT
            'clt_salario_bruto', 'clt_incluir_fgts',
            'clt_vale_alimentacao', 'clt_vale_transporte', 'clt_plano_saude', 
            'clt_plr', 'clt_outros_beneficios',
            'clt_pensao_alimenticia', 'clt_outros_descontos',
            'clt_dependentes', 'clt_anos_empresa',
            # PJ
            'pj_salario_bruto', 'pj_contador', 'pj_inss', 'pj_taxa_imposto', 
            'pj_outras_despesas', 'pj_beneficios_tributaveis', 'pj_beneficios_nao_tributaveis'
        ]
        
        widgets = {
            # CLT - Dados básicos
            'clt_salario_bruto': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0',
                'data-sync': 'salary'
            }),
            'clt_incluir_fgts': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500'
            }),
            
            # CLT - Benefícios
            'clt_vale_alimentacao': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0'
            }),
            'clt_vale_transporte': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0'
            }),
            'clt_plano_saude': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0'
            }),
            'clt_plr': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0'
            }),
            'clt_outros_beneficios': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0'
            }),
            
            # CLT - Descontos
            'clt_pensao_alimenticia': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0'
            }),
            'clt_outros_descontos': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0'
            }),
            
            # CLT - Outros dados
            'clt_dependentes': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0',
                'min': '0',
                'max': '20'
            }),
            'clt_anos_empresa': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0',
                'min': '0',
                'max': '50'
            }),
            
            # PJ - Dados básicos
            'pj_salario_bruto': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0',
                'data-sync': 'salary'
            }),
            
            # PJ - Despesas
            'pj_contador': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500',
                'placeholder': '189,00',
                'step': '0.01',
                'min': '0'
            }),
            'pj_inss': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500',
                'placeholder': '166,98',
                'step': '0.01',
                'min': '0'
            }),
            'pj_taxa_imposto': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500',
                'placeholder': '10,0',
                'step': '0.01',
                'min': '0',
                'max': '100'
            }),
            'pj_outras_despesas': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0'
            }),
            
            # PJ - Benefícios
            'pj_beneficios_tributaveis': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0'
            }),
            'pj_beneficios_nao_tributaveis': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0'
            }),
        }
        
        labels = {
            # CLT
            'clt_salario_bruto': 'Salário Bruto Mensal',
            'clt_incluir_fgts': 'Incluir FGTS',
            'clt_vale_alimentacao': 'Vale Refeição/Alimentação',
            'clt_vale_transporte': 'Vale-Transporte',
            'clt_plano_saude': 'Plano de Saúde',
            'clt_plr': 'PLR Anual',
            'clt_outros_beneficios': 'Outros Benefícios',
            'clt_pensao_alimenticia': 'Pensão Alimentícia',
            'clt_outros_descontos': 'Outros Descontos',
            'clt_dependentes': 'Número de Dependentes',
            'clt_anos_empresa': 'Anos na Empresa',
            # PJ
            'pj_salario_bruto': 'Salário Bruto Mensal',
            'pj_contador': 'Honorários Contador',
            'pj_inss': 'Contribuição INSS',
            'pj_taxa_imposto': 'Alíquota de Impostos (%)',
            'pj_outras_despesas': 'Outras Despesas',
            'pj_beneficios_tributaveis': 'Benefícios Tributáveis',
            'pj_beneficios_nao_tributaveis': 'Benefícios Não-Tributáveis',
        }

# Tooltips para os campos
FIELD_TOOLTIPS = {
    'clt_vale_transporte': 'Desconto máximo de 6% do salário bruto',
    'clt_plr': 'Participação nos Lucros e Resultados (valor bruto anual)',
    'clt_outros_beneficios': 'Qualquer benefício não-taxável adicional',
    'clt_pensao_alimenticia': 'Valor mensal da pensão alimentícia (dedutível do imposto de renda)',
    'clt_outros_descontos': 'Outros descontos mensais em folha (ex: empréstimos, convênios, coparticipação plano de saúde)',
    'clt_dependentes': 'Cada dependente reduz R$ 189,59 do imposto de renda',
    'clt_anos_empresa': 'Usado para calcular a multa rescisória (FGTS + 40%)',
    
    'pj_contador': 'Baseado no valor da mensalidade da Contabilizei.',
    'pj_inss': 'O valor padrão é 11% do salário mínimo.',
    'pj_taxa_imposto': 'O valor padrão é 11% do salário mínimo.',
    'pj_beneficios_tributaveis': 'Benefícios que são somados ao salário bruto para fins de tributação',
    'pj_beneficios_nao_tributaveis': 'Benefícios que você recebe mas não são tributados',
}