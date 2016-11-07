from django.db import models

class University(models.Model):
	nome = models.CharField('Nome da Universidade',max_length=100)
	codigo = models.CharField('Código', max_length=20)
	uf = models.CharField('UF', max_length=2)
	regiao = models.CharField('Região', max_length=20)
	tipo_ie = models.CharField('Tipo de IE', max_length=20)
	nota_geral = models.FloatField('Nota Geral')

	# Cultura Empreendedora
	nota_cult_emp = models.FloatField('Nota Cultura Empreendedora')
	postura_discente_ce = models.FloatField('Postura Discente')
	postura_docente_ce = models.FloatField('Postura Docente')
	disciplinas = models.FloatField('Disciplinas')

	# Inovacao
	nota_inovacao = models.FloatField('Nota Inovação')
	pesquisa_inovacao = models.FloatField('Pesquisa - Inovação')
	patentes_inovacao = models.FloatField('Patentes - Inovação')
	incubadas_inovacao = models.FloatField('Incubadas - Inovação')

	# Extensao
	nota_extensao = models.FloatField('Nota Extensão')
	redes_extensao = models.FloatField('Redes - Extensão')
	projetos_extensao = models.FloatField('Projetos - Extensão')

	# Infraestrutura
	nota_infraestrutura = models.FloatField('Nota Infraestrutura')
	qualidade_infra = models.FloatField('Qualidade - Infraestrutura')
	parque_tecno_infra = models.FloatField('Parque Tecnológico - Infraestrutura')

	# Internacionalizacao
	nota_internacionalizao = models.FloatField('Nota Intenacionalização')
	intercambio_inter = models.FloatField('Intercâmbio - Intenacionalização')
	pesquisas_inter = models.FloatField('Pesquisas - Intenacionalização')

	# Capital Financeiro
	nota_capital_financeiro = models.FloatField('Nota Capital Financeiro')
	orcamento_cap = models.FloatField('Orçamento - Capital Financeiro')
	endowment_cap = models.FloatField('Endowment - Capital Financeiro')

	def __str__(self):
		return self.nome