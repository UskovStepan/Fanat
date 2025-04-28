from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


menu = [
	{'title': 'О клубе', 'url_name': 'about'},
	{'title': 'Тренера', 'url_name': 'coach'},
	{'title': 'Расписание', 'url_name': 'schedule'},
	{'title': 'Цены', 'url_name': 'price'},
	{'title': 'Магазин', 'url_name': 'shop'},
	{'title': 'Вход', 'url_name': 'login'},
]

db_coach = [
	{'id': 1, 'type_sport': 'Бокс', 'name': 'Белебезьев Сергей Валерьевич'},
	{'id': 2, 'type_sport': 'Бокс', 'name': 'Мартиросян Альберт Маликсетович'},
	{'id': 3, 'type_sport': 'ММА', 'name': 'Гончаров Евгений Сергеевич'},
	{'id': 4, 'type_sport': 'Бокс', 'name': 'Лагунов Сергей Александрович'},
]

def index(request):
	data = {
			'title': 'Главная страница',
			'menu': menu,
			}
	return render(request, 'fanat_tomsk/index.html', context=data)
	
def show_about(request):

	return render(request, 'fanat_tomsk/about.html', {'title': 'О клубе'})

def show_coach(request):
	data_coach = {
		'title': 'Тренера',
		'posts': db_coach,
	}
	return render(request, 'fanat_tomsk/coach.html', context=data_coach)

def schedule(request):
	return render(request, 'fanat_tomsk/schedule.html', {'title': 'Расписание'})

def price(request):
	return render(request, 'fanat_tomsk/price.html', {'title': 'Цены'})

def shop(request):
	return render(request, 'fanat_tomsk/shop.html', {'title': 'Магазин'})

def login(request):
	return render(request, 'fanat_tomsk/login.html', {'title': 'Вход'})


def page_not_found(request, exception):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')