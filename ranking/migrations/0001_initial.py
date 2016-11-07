# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-07 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Universidade')),
                ('codigo', models.CharField(max_length=20, verbose_name='Código')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('regiao', models.CharField(max_length=20, verbose_name='Região')),
                ('tipo_ie', models.CharField(max_length=20, verbose_name='Tipo de IE')),
                ('nota_geral', models.FloatField(verbose_name='Nota Geral')),
                ('nota_cult_emp', models.FloatField(verbose_name='Nota Cultura Empreendedora')),
                ('postura_discente_ce', models.FloatField(verbose_name='Postura Discente')),
                ('postura_docente_ce', models.FloatField(verbose_name='Postura Docente')),
                ('disciplinas', models.FloatField(verbose_name='Disciplinas')),
                ('nota_inovacao', models.FloatField(verbose_name='Nota Inovação')),
                ('pesquisa_inovacao', models.FloatField(verbose_name='Pesquisa - Inovação')),
                ('patentes_inovacao', models.FloatField(verbose_name='Patentes - Inovação')),
                ('incubadas_inovacao', models.FloatField(verbose_name='Incubadas - Inovação')),
                ('nota_extensao', models.FloatField(verbose_name='Nota Extensão')),
                ('redes_extensao', models.FloatField(verbose_name='Redes - Extensão')),
                ('projetos_extensao', models.FloatField(verbose_name='Projetos - Extensão')),
                ('nota_infraestrutura', models.FloatField(verbose_name='Nota Infraestrutura')),
                ('qualidade_infra', models.FloatField(verbose_name='Qualidade - Infraestrutura')),
                ('parque_tecno_infra', models.FloatField(verbose_name='Parque Tecnológico - Infraestrutura')),
                ('nota_internacionalizao', models.FloatField(verbose_name='Nota Intenacionalização')),
                ('intercambio_inter', models.FloatField(verbose_name='Intercâmbio - Intenacionalização')),
                ('pesquisas_inter', models.FloatField(verbose_name='Pesquisas - Intenacionalização')),
                ('nota_capital_financeiro', models.FloatField(verbose_name='Nota Capital Financeiro')),
                ('orcamento_cap', models.FloatField(verbose_name='Orçamento - Capital Financeiro')),
                ('endowment_cap', models.FloatField(verbose_name='Endowment - Capital Financeiro')),
            ],
        ),
    ]