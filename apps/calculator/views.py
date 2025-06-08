from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .forms import CalculatorForm
from .utils import calculate_clt_values, calculate_pj_values

def calculator_view(request):
    """View principal da calculadora"""
    form = CalculatorForm()
    
    # Valores padrão para demonstração
    default_values = {
        'clt_salario_bruto': 8500,
        'clt_vale_alimentacao': 1500,
        'clt_vale_transporte': 500,
        'clt_plano_saude': 1000,
        'clt_outros_beneficios': 0,
        'clt_plr': 0,
        'clt_dependentes': 0,
        'pj_salario_bruto': 12000,
        'pj_contador': 500,
        'pj_inss': 1000,
        'pj_taxa_imposto': 15.5,
        'pj_outros_gastos': 0,
    }
    
    context = {
        'form': form,
        'default_values': default_values,
    }
    
    return render(request, 'calculator/calculator.html', context)

@method_decorator(csrf_exempt, name='dispatch')
class CalculateAjaxView(View):
    """View para cálculos via AJAX"""
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            # Dados CLT
            clt_data = {
                'salario_bruto': data.get('clt_salario_bruto', 0),
                'dependentes': data.get('clt_dependentes', 0),
                'vale_alimentacao': data.get('clt_vale_alimentacao', 0),
                'vale_transporte': data.get('clt_vale_transporte', 0),
                'plano_saude': data.get('clt_plano_saude', 0),
                'outros_beneficios': data.get('clt_outros_beneficios', 0),
                'plr': data.get('clt_plr', 0),
                'pensao_alimenticia': data.get('clt_pensao_alimenticia', 0),
                'outros_descontos': data.get('clt_outros_descontos', 0),
                'anos_empresa': data.get('clt_anos_empresa', 0),
                'incluir_fgts': data.get('clt_incluir_fgts', True),
            }
            
            # Dados PJ
            pj_data = {
                'faturamento_bruto': data.get('pj_salario_bruto', 0),
                'contador': data.get('pj_contador', 189),
                'inss': data.get('pj_inss', 166.98),
                'taxa_imposto': data.get('pj_taxa_imposto', 10),
                'outras_despesas': data.get('pj_outras_despesas', 0),
                'beneficios_tributaveis': data.get('pj_beneficios_tributaveis', 0),
                'beneficios_nao_tributaveis': data.get('pj_beneficios_nao_tributaveis', 0),
            }
            
            # Calcular resultados
            clt_result = calculate_clt_values(**clt_data)
            pj_result = calculate_pj_values(**pj_data)
            
            # Diferenças
            diferenca_mensal = pj_result['liquido_mensal'] - clt_result['liquido_mensal']
            diferenca_anual = pj_result['liquido_anual'] - clt_result['liquido_anual']
            
            response_data = {
                'success': True,
                'clt': {
                    'bruto': float(clt_result['salario_bruto']),
                    'inss': float(clt_result['inss']),
                    'irrf': float(clt_result['irrf']),
                    'desconto_vt': float(clt_result['desconto_vt']),
                    'fgts': float(clt_result['fgts']),
                    'liquido_mensal': float(clt_result['liquido_mensal']),
                    'liquido_anual': float(clt_result['liquido_anual']),
                    'decimo_terceiro': float(clt_result['decimo_terceiro']),
                    'ferias': float(clt_result['ferias']),
                    'beneficios_mensais': float(clt_result['beneficios_mensais']),
                    'vale_alimentacao': float(clt_result['vale_alimentacao']),
                    'vale_transporte': float(clt_result['vale_transporte']),
                    'plano_saude': float(clt_result['plano_saude']),
                },
                'pj': {
                    'bruto': float(pj_result['faturamento_bruto']),
                    'impostos': float(pj_result['impostos']),
                    'contador': float(pj_result['contador']),
                    'inss': float(pj_result['inss']),
                    'outras_despesas': float(pj_result['outras_despesas']),
                    'liquido_mensal': float(pj_result['liquido_mensal']),
                    'liquido_anual': float(pj_result['liquido_anual']),
                },
                'comparacao': {
                    'diferenca_mensal': float(diferenca_mensal),
                    'diferenca_anual': float(diferenca_anual),
                    'percentual_diferenca': float((diferenca_anual / clt_result['liquido_anual']) * 100) if clt_result['liquido_anual'] > 0 else 0,
                    'melhor_opcao': 'PJ' if diferenca_anual > 0 else 'CLT',
                }
            }
            
            return JsonResponse(response_data)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)
