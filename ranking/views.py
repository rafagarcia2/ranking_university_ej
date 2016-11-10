from django.shortcuts import render
from .models import University

def page_index(request):
	universidades = University.objects.all()
	
	univ_geral = universidades.order_by('-nota_geral')
	univ_cultura = universidades.order_by('-nota_cult_emp')
	univ_inovacao = universidades.order_by('-nota_inovacao')
	univ_extensao = universidades.order_by('-nota_extensao')
	univ_infraestrutura = universidades.order_by('-nota_infraestrutura')
	univ_internacionalizao = universidades.order_by('-nota_internacionalizao')
	univ_capital = universidades.order_by('-nota_capital_financeiro')
	
	return render(request, 'ranking/index.html', 
		{'univ_geral': univ_geral, 'univ_cultura': univ_cultura, 'univ_inovacao': univ_inovacao,
		'univ_extensao': univ_extensao, 'univ_infraestrutura': univ_infraestrutura,
		'univ_internacionalizao': univ_internacionalizao, 'univ_capital': univ_capital})

# Nao estam sendo usados
def ranking_geral(request):
	universidades = University.objects.all().order_by('-nota_geral')
	return render(request, 'ranking/ranking_geral.html', {'universidades': universidades})

def ranking_cultura(request):
	universidades = University.objects.all().order_by('-nota_cult_emp')
	return render(request, 'ranking/ranking_cultura.html', {'universidades': universidades})

def ranking_inovacao(request):
	universidades = University.objects.all().order_by('-nota_inovacao')
	return render(request, 'ranking/ranking_inovacao.html', {'universidades': universidades})

def ranking_extensao(request):
	universidades = University.objects.all().order_by('-nota_extensao')
	return render(request, 'ranking/ranking_extensao.html', {'universidades': universidades})

def ranking_infraestrutura(request):
	universidades = University.objects.all().order_by('-nota_infraestrutura')
	return render(request, 'ranking/ranking_infraestrutura.html', {'universidades': universidades})

def ranking_internacionalizacao(request):
	universidades = University.objects.all().order_by('-nota_internacionalizao')
	return render(request, 'ranking/ranking_internacionalizacao.html', {'universidades': universidades})

def ranking_capital(request):
	universidades = University.objects.all().order_by('-nota_capital_financeiro')
	return render(request, 'ranking/ranking_capital.html', {'universidades': universidades})