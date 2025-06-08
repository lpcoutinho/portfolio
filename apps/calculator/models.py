from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class CalculatorResult(models.Model):
    """
    Modelo para armazenar resultados de cálculos CLT vs PJ
    """
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Dados CLT
    clt_salario_bruto = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Salário Bruto Mensal"
    )
    clt_incluir_fgts = models.BooleanField(
        default=True,
        verbose_name="Incluir FGTS"
    )
    
    # Benefícios CLT
    clt_vale_alimentacao = models.DecimalField(
        max_digits=8, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Vale Refeição/Alimentação"
    )
    clt_vale_transporte = models.DecimalField(
        max_digits=8, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Vale-Transporte"
    )
    clt_plano_saude = models.DecimalField(
        max_digits=8, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Plano de Saúde"
    )
    clt_plr = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="PLR Anual"
    )
    clt_outros_beneficios = models.DecimalField(
        max_digits=8, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Outros Benefícios"
    )
    
    # Descontos CLT
    clt_pensao_alimenticia = models.DecimalField(
        max_digits=8, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Pensão Alimentícia"
    )
    clt_outros_descontos = models.DecimalField(
        max_digits=8, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Outros Descontos"
    )
    
    # Outros dados CLT
    clt_dependentes = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(20)],
        verbose_name="Número de Dependentes"
    )
    clt_anos_empresa = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        verbose_name="Anos na Empresa"
    )
    
    # Dados PJ
    pj_salario_bruto = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Salário Bruto Mensal"
    )
    
    # Despesas PJ
    pj_contador = models.DecimalField(
        max_digits=8, decimal_places=2, default=189,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Honorários Contador"
    )
    pj_inss = models.DecimalField(
        max_digits=8, decimal_places=2, default=166.98,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Contribuição INSS"
    )
    pj_taxa_imposto = models.DecimalField(
        max_digits=5, decimal_places=2, default=10,
        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('100'))],
        verbose_name="Alíquota de Impostos (%)"
    )
    pj_outras_despesas = models.DecimalField(
        max_digits=8, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Outras Despesas"
    )
    
    # Benefícios PJ
    pj_beneficios_tributaveis = models.DecimalField(
        max_digits=8, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Benefícios Tributáveis"
    )
    pj_beneficios_nao_tributaveis = models.DecimalField(
        max_digits=8, decimal_places=2, default=0,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Benefícios Não-Tributáveis"
    )
    
    # Resultados calculados (armazenados para histórico)
    clt_liquido_mensal = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        verbose_name="CLT Líquido Mensal"
    )
    clt_liquido_anual = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True,
        verbose_name="CLT Líquido Anual"
    )
    pj_liquido_mensal = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        verbose_name="PJ Líquido Mensal"
    )
    pj_liquido_anual = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True,
        verbose_name="PJ Líquido Anual"
    )
    diferenca_mensal = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        verbose_name="Diferença Mensal"
    )
    diferenca_anual = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True,
        verbose_name="Diferença Anual"
    )
    
    class Meta:
        verbose_name = "Resultado da Calculadora"
        verbose_name_plural = "Resultados da Calculadora"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Cálculo {self.created_at.strftime('%d/%m/%Y %H:%M')}"
    
    def calculate_clt(self):
        """Calcula valores líquidos CLT"""
        from .utils import calculate_clt_values
        return calculate_clt_values(
            salario_bruto=self.clt_salario_bruto,
            dependentes=self.clt_dependentes,
            vale_alimentacao=self.clt_vale_alimentacao,
            vale_transporte=self.clt_vale_transporte,
            plano_saude=self.clt_plano_saude,
            outros_beneficios=self.clt_outros_beneficios,
            plr=self.clt_plr,
            pensao_alimenticia=self.clt_pensao_alimenticia,
            outros_descontos=self.clt_outros_descontos,
            anos_empresa=self.clt_anos_empresa,
            incluir_fgts=self.clt_incluir_fgts
        )
    
    def calculate_pj(self):
        """Calcula valores líquidos PJ"""
        from .utils import calculate_pj_values
        return calculate_pj_values(
            faturamento_bruto=self.pj_salario_bruto,
            contador=self.pj_contador,
            inss=self.pj_inss,
            taxa_imposto=self.pj_taxa_imposto,
            outras_despesas=self.pj_outras_despesas,
            beneficios_tributaveis=self.pj_beneficios_tributaveis,
            beneficios_nao_tributaveis=self.pj_beneficios_nao_tributaveis
        )
    
    def save(self, *args, **kwargs):
        """Override save para calcular valores antes de salvar"""
        clt_result = self.calculate_clt()
        pj_result = self.calculate_pj()
        
        self.clt_liquido_mensal = clt_result['liquido_mensal']
        self.clt_liquido_anual = clt_result['liquido_anual']
        self.pj_liquido_mensal = pj_result['liquido_mensal']
        self.pj_liquido_anual = pj_result['liquido_anual']
        self.diferenca_mensal = self.pj_liquido_mensal - self.clt_liquido_mensal
        self.diferenca_anual = self.pj_liquido_anual - self.clt_liquido_anual
        
        super().save(*args, **kwargs)
