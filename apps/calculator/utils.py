"""
Utilitários para cálculos da calculadora CLT vs PJ
"""
from decimal import Decimal, ROUND_HALF_UP

def calculate_clt_values(salario_bruto, dependentes=0, vale_alimentacao=0, vale_transporte=0, 
                        plano_saude=0, outros_beneficios=0, plr=0, pensao_alimenticia=0, 
                        outros_descontos=0, anos_empresa=0, incluir_fgts=True):
    """
    Calcula valores líquidos para CLT baseado na legislação brasileira
    """
    salario_bruto = Decimal(str(salario_bruto))
    dependentes = int(dependentes)
    vale_alimentacao = Decimal(str(vale_alimentacao))
    vale_transporte = Decimal(str(vale_transporte))
    plano_saude = Decimal(str(plano_saude))
    outros_beneficios = Decimal(str(outros_beneficios))
    plr = Decimal(str(plr))
    pensao_alimenticia = Decimal(str(pensao_alimenticia))
    outros_descontos = Decimal(str(outros_descontos))
    anos_empresa = int(anos_empresa)
    
    # Cálculo INSS CLT (2024)
    inss = calculate_inss_clt(salario_bruto)
    
    # Desconto Vale Transporte (máximo 6% do salário)
    desconto_vt = min(vale_transporte, salario_bruto * Decimal('0.06'))
    
    # Base de cálculo IRRF (salário - INSS - dependentes - pensão alimentícia)
    deducao_dependente = Decimal('189.59') * dependentes
    base_irrf = salario_bruto - inss - deducao_dependente - pensao_alimenticia
    
    # Cálculo IRRF
    irrf = calculate_irrf(base_irrf)
    
    # FGTS (8% do salário bruto)
    fgts_mensal = salario_bruto * Decimal('0.08') if incluir_fgts else Decimal('0')
    
    # Salário líquido mensal (sem benefícios)
    liquido_mensal_base = salario_bruto - inss - irrf - pensao_alimenticia - outros_descontos - desconto_vt
    
    # Salário líquido com benefícios
    liquido_mensal = liquido_mensal_base + vale_alimentacao + vale_transporte + plano_saude + outros_beneficios
    
    # Cálculo anual (13º salário + férias + PLR)
    decimo_terceiro_bruto = salario_bruto
    decimo_terceiro_inss = calculate_inss_clt(decimo_terceiro_bruto)
    decimo_terceiro_irrf = calculate_irrf(decimo_terceiro_bruto - decimo_terceiro_inss - deducao_dependente - pensao_alimenticia)
    decimo_terceiro_liquido = decimo_terceiro_bruto - decimo_terceiro_inss - decimo_terceiro_irrf
    
    # Férias (1/3 a mais)
    ferias_bruto = salario_bruto + (salario_bruto / 3)
    ferias_inss = calculate_inss_clt(ferias_bruto)
    ferias_irrf = calculate_irrf(ferias_bruto - ferias_inss - deducao_dependente - pensao_alimenticia)
    ferias_liquido = ferias_bruto - ferias_inss - ferias_irrf
    
    # FGTS anual (incluindo 13º e férias)
    fgts_anual = (salario_bruto * 12 + decimo_terceiro_bruto + ferias_bruto) * Decimal('0.08') if incluir_fgts else Decimal('0')
    
    # Multa rescisória FGTS (40% sobre FGTS acumulado)
    fgts_acumulado = fgts_anual * anos_empresa if anos_empresa > 0 else fgts_anual
    multa_fgts = fgts_acumulado * Decimal('0.40') if incluir_fgts else Decimal('0')
    
    liquido_anual = (liquido_mensal_base * 12) + decimo_terceiro_liquido + ferias_liquido + plr
    liquido_anual_com_beneficios = liquido_anual + (vale_alimentacao + vale_transporte + plano_saude + outros_beneficios) * 12
    
    return {
        'salario_bruto': salario_bruto,
        'inss': inss,
        'irrf': irrf,
        'desconto_vt': desconto_vt,
        'fgts': fgts_mensal,
        'liquido_mensal': liquido_mensal_base.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'liquido_mensal_com_beneficios': liquido_mensal.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'liquido_anual': liquido_anual.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'liquido_anual_com_beneficios': liquido_anual_com_beneficios.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'decimo_terceiro': decimo_terceiro_liquido.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'ferias': ferias_liquido.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'fgts_anual': fgts_anual.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'multa_fgts': multa_fgts.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'beneficios_mensais': vale_alimentacao + vale_transporte + plano_saude + outros_beneficios,
        'vale_alimentacao': vale_alimentacao,
        'vale_transporte': vale_transporte,
        'plano_saude': plano_saude,
    }

def calculate_pj_values(faturamento_bruto, contador=189, inss=166.98, taxa_imposto=10, 
                       outras_despesas=0, beneficios_tributaveis=0, beneficios_nao_tributaveis=0):
    """
    Calcula valores líquidos para PJ (Simples Nacional)
    """
    faturamento_bruto = Decimal(str(faturamento_bruto))
    contador = Decimal(str(contador))
    inss = Decimal(str(inss))
    taxa_imposto = Decimal(str(taxa_imposto))
    outras_despesas = Decimal(str(outras_despesas))
    beneficios_tributaveis = Decimal(str(beneficios_tributaveis))
    beneficios_nao_tributaveis = Decimal(str(beneficios_nao_tributaveis))
    
    # Base tributável (faturamento + benefícios tributáveis)
    base_tributavel = faturamento_bruto + beneficios_tributaveis
    
    # Cálculo dos impostos (Simples Nacional)
    impostos = base_tributavel * (taxa_imposto / 100)
    
    # Líquido mensal
    liquido_mensal = faturamento_bruto - impostos - contador - inss - outras_despesas + beneficios_nao_tributaveis
    
    # Líquido anual (sem 13º e férias)
    liquido_anual = liquido_mensal * 12
    
    return {
        'faturamento_bruto': faturamento_bruto,
        'base_tributavel': base_tributavel,
        'impostos': impostos.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'contador': contador,
        'inss': inss,
        'outras_despesas': outras_despesas,
        'beneficios_tributaveis': beneficios_tributaveis,
        'beneficios_nao_tributaveis': beneficios_nao_tributaveis,
        'liquido_mensal': liquido_mensal.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'liquido_anual': liquido_anual.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'bruto': faturamento_bruto,  # Para compatibilidade
    }

def calculate_inss_clt(salario):
    """
    Calcula INSS CLT baseado na tabela 2024
    """
    salario = Decimal(str(salario))
    
    if salario <= Decimal('1412.00'):
        return salario * Decimal('0.075')
    elif salario <= Decimal('2666.68'):
        return (Decimal('1412.00') * Decimal('0.075')) + \
               ((salario - Decimal('1412.00')) * Decimal('0.09'))
    elif salario <= Decimal('4000.03'):
        return (Decimal('1412.00') * Decimal('0.075')) + \
               ((Decimal('2666.68') - Decimal('1412.00')) * Decimal('0.09')) + \
               ((salario - Decimal('2666.68')) * Decimal('0.12'))
    elif salario <= Decimal('7786.02'):
        return (Decimal('1412.00') * Decimal('0.075')) + \
               ((Decimal('2666.68') - Decimal('1412.00')) * Decimal('0.09')) + \
               ((Decimal('4000.03') - Decimal('2666.68')) * Decimal('0.12')) + \
               ((salario - Decimal('4000.03')) * Decimal('0.14'))
    else:
        # Teto do INSS
        return Decimal('908.85')

def calculate_irrf(base_calculo):
    """
    Calcula IRRF baseado na tabela 2024
    """
    base_calculo = Decimal(str(base_calculo))
    
    if base_calculo <= Decimal('2259.20'):
        return Decimal('0')
    elif base_calculo <= Decimal('2826.65'):
        return (base_calculo * Decimal('0.075')) - Decimal('169.44')
    elif base_calculo <= Decimal('3751.05'):
        return (base_calculo * Decimal('0.15')) - Decimal('381.44')
    elif base_calculo <= Decimal('4664.68'):
        return (base_calculo * Decimal('0.225')) - Decimal('662.77')
    else:
        return (base_calculo * Decimal('0.275')) - Decimal('896.00')