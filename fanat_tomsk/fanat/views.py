from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from .models import Probnic


menu = [
	{'title': 'О клубе', 'url_name': 'about'},
	{'title': 'Тренера', 'url_name': 'coach'},
	{'title': 'Расписание', 'url_name': 'schedule'},
	{'title': 'Цены', 'url_name': 'price'},
	{'title': 'Магазин', 'url_name': 'shop'},
	{'title': 'Вход', 'url_name': 'login'}
]

db_coach = [
	{'id': 1, 'type_sport': 'Бокс', 'name': 'Белебезьев Сергей Валерьевич', 'url_name': 'Sergey_Belebezyev' },
	{'id': 2, 'type_sport': 'Самбо', 'name': 'Очередько Антон', 'url_name': 'Anton_Ocheredko'},
	{'id': 3, 'type_sport': 'ММА', 'name': 'Кишкин Степан', 'url_name': 'Stepan Kishkin' },
	{'id': 4, 'type_sport': 'Бокс', 'name': 'Толстых Кирилл', 'url_name': 'Kirill_Tolstykh'},
]



def index(request):
	data = {
			'title': 'Главная страница',
			'menu': menu,
			}
	return render(request, 'fanat_tomsk/index.html', context=data)
	

def show_about(request):
	return render(request, 'fanat_tomsk/about.html', {'menu': menu, 'title': 'О клубе'})


def show_coach(request):
	data_coach = {
		'menu': menu,
		'title': 'Тренера',
		'db_coach': db_coach,
	}
	return render(request, 'fanat_tomsk/coach.html', context=data_coach)


def show_coachview(request, coach_slug):
	post = get_object_or_404(Probnic, slug=coach_slug)
	data = {
		'title': post.title,
		'menu': menu, 
		'post': post,
		'cat_selected': 1,
	}
	return render(request, 'fanat_tomsk/coach.html', data)


def schedule(request):
	return render(request, 'fanat_tomsk/schedule.html', {'menu': menu, 'title': 'Расписание'})


def price(request):
	return render(request, 'fanat_tomsk/price.html', {'menu': menu, 'title': 'Цены'})


def shop(request):
	return render(request, 'fanat_tomsk/shop.html', {'menu': menu, 'title': 'Магазин'})


def login(request):
	return render(request, 'fanat_tomsk/login.html', {'menu': menu, 'title': 'Вход'})


def page_not_found(request, exception):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')