from django.shortcuts import render
from .models import University


def ranking_geral(request):
	universidades = University.objects.all().order_by('nota_geral')
	return render(request, 'ranking/ranking_geral.html', {'universidades': universidades})

def ranking_cultura(request):
	universidades = University.objects.all().order_by('nota_cult_emp')
	return render(request, 'ranking/ranking_cultura.html', {'universidades': universidades})

def ranking_inovacao(request):
	universidades = University.objects.all().order_by('nota_inovacao')
	return render(request, 'ranking/ranking_inovacao.html', {'universidades': universidades})

def ranking_extensao(request):
	universidades = University.objects.all().order_by('nota_extensao')
	return render(request, 'ranking/ranking_extensao.html', {'universidades': universidades})

def ranking_infraestrutura(request):
	universidades = University.objects.all().order_by('nota_infraestrutura')
	return render(request, 'ranking/ranking_infraestrutura.html', {'universidades': universidades})

def ranking_internacionalizacao(request):
	universidades = University.objects.all().order_by('nota_internacionalizao')
	return render(request, 'ranking/ranking_internacionalizacao.html', {'universidades': universidades})

def ranking_capital(request):
	universidades = University.objects.all().order_by('nota_capital_financeiro')
	return render(request, 'ranking/ranking_capital.html', {'universidades': universidades})
