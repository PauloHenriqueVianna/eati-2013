from __future__ import unicode_literals

from django.db import models

class Categorias(models.Model):
    id_categoria = models.IntegerField(primary_key=True, db_column='ID_CATEGORIA')
    id_evento = models.ForeignKey('EventosInscricao', db_column='ID_EVENTO')
    descr_categoria = models.CharField(max_length=100L, db_column='DESCR_CATEGORIA')
    vl_categoria = models.DecimalField(decimal_places=2, max_digits=9, db_column='VL_CATEGORIA')
    class Meta:
        db_table = 'CATEGORIAS'

class Estados(models.Model):
    uf = models.CharField(max_length=2L, primary_key=True, db_column='UF')
    nome = models.CharField(max_length=100L, db_column='NOME')
    class Meta:
        db_table = 'ESTADOS'

class EventosInscricao(models.Model):
    id_evento = models.IntegerField(primary_key=True, db_column='ID_EVENTO')
    nome_evento = models.CharField(max_length=100L, db_column='NOME_EVENTO')
    senha = models.CharField(max_length=32L, db_column='SENHA', blank=True)
    dt_hr_limite_inscr = models.DateTimeField(db_column='DT_HR_LIMITE_INSCR')
    dt_vcto_boleto = models.DateField(db_column='DT_VCTO_BOLETO')
    ult_nr_inscr = models.IntegerField(db_column='ULT_NR_INSCR')
    class Meta:
        db_table = 'EVENTOS_INSCRICAO'

class IdsDisponiveis(models.Model):
    nome_tabela = models.CharField(max_length=30L, primary_key=True, db_column='NOME_TABELA')
    campo_chave = models.CharField(max_length=30L, db_column='CAMPO_CHAVE')
    ult_id = models.IntegerField(db_column='ULT_ID')
    class Meta:
        db_table = 'IDS_DISPONIVEIS'

class Pagamentos(models.Model):
    id_evento = models.ForeignKey(EventosInscricao, db_column='ID_EVENTO')
    num_inscricao = models.IntegerField(db_column='NUM_INSCRICAO')
    dt_pagamento = models.DateField(null=True, db_column='DT_PAGAMENTO', blank=True)
    vl_recebido = models.DecimalField(decimal_places=2, null=True, max_digits=9, db_column='VL_RECEBIDO', blank=True)
    ind_origem = models.CharField(max_length=1L, db_column='IND_ORIGEM')
    class Meta:
        db_table = 'PAGAMENTOS'

class Participantes(models.Model):
    id_participante = models.IntegerField(primary_key=True, db_column='ID_PARTICIPANTE')
    id_categoria = models.ForeignKey(Categorias, db_column='ID_CATEGORIA') 
    email = models.CharField(max_length=200L, db_column='EMAIL')
    num_inscricao = models.IntegerField(db_column='NUM_INSCRICAO')
    nome = models.CharField(max_length=100L, db_column='NOME')
    sexo = models.CharField(max_length=1L, db_column='SEXO')
    instituicao = models.CharField(max_length=100L, db_column='INSTITUICAO', blank=True)
    endereco = models.CharField(max_length=100L, db_column='ENDERECO', blank=True)
    complemento = models.CharField(max_length=100L, db_column='COMPLEMENTO', blank=True)
    cep = models.CharField(max_length=10L, db_column='CEP', blank=True)
    cidade = models.CharField(max_length=100L, db_column='CIDADE', blank=True)
    uf = models.ForeignKey(Estados, null=True, db_column='UF', blank=True)
    class Meta:
        db_table = 'PARTICIPANTES'

    def getSexo(self):
        if self.sexo == 'M':
            return 'Masculino'
        else:
            return 'Feminino'

class AtividadesAdicionais(models.Model):
    id_atividade = models.IntegerField(primary_key=True, db_column='ID_ATIVIDADE')
    id_evento = models.ForeignKey('EventosInscricao', db_column='ID_EVENTO')
    descr_atividade = models.CharField(max_length=100L, db_column='DESCR_ATIVIDADE')
    obs_atividade = models.TextField(db_column='OBS_ATIVIDADE', blank=True)
    vl_atividade = models.DecimalField(decimal_places=2, max_digits=9, db_column='VL_ATIVIDADE')
    vagas = models.IntegerField(null=True, db_column='VAGAS', blank=True)
    atividades= models.ManyToManyField(Participantes, through='ParticipantesAtividades')
    class Meta:
        db_table = 'ATIVIDADES_ADICIONAIS'

    def haVagas(self):
        inscritos = ParticipantesAtividades.objects.filter(id_atividade=self.id_atividade).count()
        if inscritos >= self.vagas:
            return False
        else:
            return True

class ParticipantesAtividades(models.Model):
    id_participante = models.ForeignKey(Participantes, db_column='ID_PARTICIPANTE')
    id_atividade = models.ForeignKey(AtividadesAdicionais, db_column='ID_ATIVIDADE')
    class Meta:
        db_table = 'PARTICIPANTES_ATIVIDADES'

class Pesquisa(models.Model):
    id_participante = models.ForeignKey(Participantes, primary_key=True, db_column='ID_PARTICIPANTE')
    ind_certificado = models.CharField(max_length=1L, db_column='IND_CERTIFICADO', blank=True)
    ind_avaliacao_geral = models.CharField(max_length=1L, db_column='IND_AVALIACAO_GERAL', blank=True)
    ind_programacao = models.CharField(max_length=1L, db_column='IND_PROGRAMACAO', blank=True)
    ind_infra = models.CharField(max_length=1L, db_column='IND_INFRA', blank=True)
    ind_cofee = models.CharField(max_length=1L, db_column='IND_COFEE', blank=True)
    ind_valor = models.CharField(max_length=1L, db_column='IND_VALOR', blank=True)
    ind_prox_eati = models.CharField(max_length=1L, db_column='IND_PROX_EATI', blank=True)
    avaliacao = models.TextField(db_column='AVALIACAO', blank=True)
    data_hora = models.DateTimeField(db_column='DATA_HORA')
    class Meta:
        db_table = 'PESQUISA'

class PesquisaBkp(models.Model):
    id_participante = models.IntegerField(db_column='ID_PARTICIPANTE')
    ind_certificado = models.CharField(max_length=1L, db_column='IND_CERTIFICADO', blank=True)
    ind_avaliacao_geral = models.CharField(max_length=1L, db_column='IND_AVALIACAO_GERAL', blank=True)
    ind_programacao = models.CharField(max_length=1L, db_column='IND_PROGRAMACAO', blank=True)
    ind_infra = models.CharField(max_length=1L, db_column='IND_INFRA', blank=True)
    ind_cofee = models.CharField(max_length=1L, db_column='IND_COFEE', blank=True)
    ind_valor = models.CharField(max_length=1L, db_column='IND_VALOR', blank=True)
    ind_prox_eati = models.CharField(max_length=1L, db_column='IND_PROX_EATI', blank=True)
    avaliacao = models.TextField(db_column='AVALIACAO', blank=True)
    data_hora = models.DateTimeField(db_column='DATA_HORA')
    class Meta:
        db_table = 'PESQUISA_BKP'

class Presencas(models.Model):
    id_participante = models.ForeignKey(Participantes, db_column='ID_PARTICIPANTE')
    id_atividade = models.ForeignKey(AtividadesAdicionais, null=True, db_column='ID_ATIVIDADE', blank=True)
    data_hora = models.DateTimeField(db_column='DATA_HORA')
    class Meta:
        db_table = 'PRESENCAS'

class VPagamentos(models.Model):
    id_evento = models.IntegerField(db_column='ID_EVENTO')
    id_participante = models.IntegerField(db_column='ID_PARTICIPANTE')
    num_inscricao = models.IntegerField(db_column='NUM_INSCRICAO')
    nome = models.CharField(max_length=100L, db_column='NOME')
    instituicao = models.CharField(max_length=100L, db_column='INSTITUICAO', blank=True)
    descr_categoria = models.CharField(max_length=100L, db_column='DESCR_CATEGORIA')
    vl_categoria = models.DecimalField(decimal_places=2, max_digits=9, db_column='VL_CATEGORIA')
    minicursos = models.BigIntegerField(db_column='MINICURSOS')
    vl_minicursos = models.DecimalField(decimal_places=2, null=True, max_digits=31, db_column='VL_MINICURSOS', blank=True)
    dt_pagamento = models.DateField(null=True, db_column='DT_PAGAMENTO', blank=True)
    vl_recebido = models.DecimalField(decimal_places=2, null=True, max_digits=9, db_column='VL_RECEBIDO', blank=True)
    ind_origem = models.CharField(max_length=1L, db_column='IND_ORIGEM', blank=True)
    class Meta:
        db_table = 'V_PAGAMENTOS'

