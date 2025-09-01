from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

import logging

from .models import Coach_new, WeekDay, Schedule, WorkoutType


menu = [
	{'title': 'О клубе', 'url_name': 'about'},
	{'title': 'Тренера', 'url_name': 'coach'},
	{'title': 'Расписание', 'url_name': 'schedule'},
	{'title': 'Цены', 'url_name': 'price'},
	{'title': 'Магазин', 'url_name': 'shop'},
	{'title': 'Вход', 'url_name': 'login'}
]

# db_coach = [
# 	{'id': 1, 'type_sport': 'Бокс', 'name': 'Белебезьев Сергей Валерьевич', 'url_name': 'Sergey_Belebezyev' },
# 	{'id': 2, 'type_sport': 'Самбо', 'name': 'Очередько Антон', 'url_name': 'Anton_Ocheredko'},
# 	{'id': 3, 'type_sport': 'ММА', 'name': 'Кишкин Степан', 'url_name': 'Stepan_Kishkin' },
# 	{'id': 4, 'type_sport': 'Бокс', 'name': 'Толстых Кирилл', 'url_name': 'Kirill_Tolstykh'},
# ]



def index(request):
	data = {
			'title': 'Главная страница',
			'menu': menu,
			}
	return render(request, 'fanat_tomsk/index.html', context=data)
	

def show_about(request):
	return render(request, 'fanat_tomsk/about.html', {'menu': menu, 'title': 'О клубе'})


def coach(request):
    coaches = Coach_new.published.all()
    # return render(request, 'fanat_tomsk/coach.html', {
    #     'title': 'Тренеры',
    #     'menu': menu,
    #     'db_coach': coaches,
    # })
    data = {
		'title': 'Тренера',
		'db_coach': coaches,
		'menu': menu,
	}
    return render(request, 'fanat_tomsk/coach.html', data)

def show_coach(request, slug):
    coach = get_object_or_404(Coach_new, slug=slug)
    data = {
		'title': coach.name,
		'menu': menu,
		'coach': coach,
	}
    return render(request, 'fanat_tomsk/show_coach.html', data)


def schedule(request):
    days = WeekDay.objects.all()
    workout_types = WorkoutType.objects.all()
    schedules = Schedule.objects.select_related(
		'weekday', 'workout_type', 'trainer'
	).all()
    schedule_by_day ={}
    for day in days:
        day_schedules = schedules.filter(weekday = day).order_by('start_time')
        schedule_by_day[day] = day_schedules
        
    context = {
		'days': days,
		'workout_types': workout_types,
		'schedule_by_day': schedule_by_day,
		'title': 'Расписание тренеровок',
		'menu': menu
	}
    
    return render(request, 'fanat_tomsk/schedule.html', context)


def price(request):
	return render(request, 'fanat_tomsk/price.html', {'menu': menu, 'title': 'Цены'})


def shop(request):
	return render(request, 'fanat_tomsk/shop.html', {'menu': menu, 'title': 'Магазин'})


def login(request):
	return render(request, 'fanat_tomsk/login.html', {'menu': menu, 'title': 'Вход'})


def page_not_found(request, exception):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')