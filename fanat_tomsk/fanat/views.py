from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Coach


menu = [
	{'title': 'О клубе', 'url_name': 'about'},
	{'title': 'Тренера', 'url_name': 'coach'},
	{'title': 'Расписание', 'url_name': 'schedule'},
	{'title': 'Цены', 'url_name': 'price'},
	{'title': 'Магазин', 'url_name': 'shop'},
	{'title': 'Вход', 'url_name': 'login'}
]

# db_coach = [
# 	{'id': 1, 'type_sport': 'Бокс', 'name': 'Белебезьев Сергей Валерьевич'},
# 	{'id': 2, 'type_sport': 'Бокс', 'name': 'Мартиросян Альберт Маликсетович'},
# 	{'id': 3, 'type_sport': 'ММА', 'name': 'Гончаров Евгений Сергеевич'},
# 	{'id': 4, 'type_sport': 'Бокс', 'name': 'Лагунов Сергей Александрович'}
# ]

db_coach = [
	{'id': 1, 'type_sport': 'Бокс', 'name': 'Майк Тайсон', 'titul': 'КМС по боксу, 2-х кратный чемпион сибирского федерального округа в тяжелом весе'},
	{'id': 2, 'type_sport': 'Бокс', 'name': 'Флойд Майвезер', 'titul': 'МС международного класса по боксу, 2-х кратный чемпион России'},
	{'id': 3, 'type_sport': 'Бокс', 'name': 'Геннадий Головкин', 'titul': 'Серебряный призёр Олимпийских игр, чемпион мира в категории любителей. Среди профессионалов двукратный чемпион мира по версиям IBF, WBA и IBO.' },
	{'id': 4, 'type_sport': 'Самбо', 'name': 'Федор Емельянинко', 'titul': 'четырёхкратный чемпион мира по смешанным боевым искусствам — ММА в тяжёлом весе по версии Pride FC, двукратный — по версии RINGS, двукратный — по версии WAMMA, четырёхкратный чемпион мира и девятикратный чемпион России по боевому самбо.' },
	{'id': 5, 'type_sport': 'ММА', 'name': 'Хабиб Нурмагомедов', 'titul': 'Бывший чемпион UFC в лёгком весе. Рейтинг Sherdog ставил Нурмагомедова на первое место как в лёгком весе, так и в списке лучших бойцов вне зависимости от весовой категории'},
	{'id': 6, 'type_sport': 'ММА', 'name': 'Конор Макгрегор', 'titul': 'Первый в истории UFC двойной чемпион, владевший одновременно двумя поясами в разных весовых категориях — полулёгкой и лёгкой.'},
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
		'posts': db_coach,
	}
	return render(request, 'fanat_tomsk/coach.html', context=data_coach)

def coach_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coach_template.html', {'coach_list': coaches})


def show_coachview(request, coach_id):
	return show_coach(request)


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