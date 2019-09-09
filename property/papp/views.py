# encoding: utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Flat, FlatOrder, House, HouseOrder, Parking, ParkingOrder, Land, LandOrder
from .models import Commercial, CommercialOrder, Industry, IndustryOrder, Auto, AutoOrder
from .models import Equipment, EquipmentOrder
from .forms import UserLoginForm, UserRegisterForm, UpdateProfileForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout)
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.core.mail import send_mail
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

def index(request):
	if request.method == 'POST':
		city = request.POST.get('city')
		area_min = request.POST.get('area_min')
		area_max = request.POST.get('area_max')
		price_min = request.POST.get('price_min')
		price_max = request.POST.get('price_max')
		constYear_min = request.POST.get('constYear_min')
		constYear_max = request.POST.get('constYear_max')
		roomNumber = request.POST.get('roomNumber')
		storey = request.POST.get('storey')

		flats = Flat.objects.filter(city=city, area__gte=area_min, 
			area__lte=area_max, price__gte=price_min, price__lte=price_max, 
			constYear__gte=constYear_min, constYear__lte=constYear_max, 
			roomNumber=roomNumber, storey=storey)
	else:
		flats = Flat.objects.all().order_by('-id') # ordering from oldest to newest
	flats_popular = Flat.objects.order_by('-id')[:4]
	context = {
			'flats': flats,
			'flats_popular': flats_popular,
		}
	return render(request, 'papp/index.html', context)

def house(request):
	if request.method == 'POST':
		city = request.POST.get('city')
		area_min = request.POST.get('area_min')
		area_max = request.POST.get('area_max')
		price_min = request.POST.get('price_min')
		price_max = request.POST.get('price_max')
		constYear_min = request.POST.get('constYear_min')
		constYear_max = request.POST.get('constYear_max')
		roomNumber = request.POST.get('roomNumber')
		storeyNumber = request.POST.get('storeyNumber')

		houses = House.objects.filter(city=city, area__gte=area_min, 
			area__lte=area_max, price__gte=price_min, price__lte=price_max, 
			constYear__gte=constYear_min, constYear__lte=constYear_max, 
			roomNumber=roomNumber, storeyNumber=storeyNumber)
	else:
		houses = House.objects.all().order_by('-id') # ordering from oldest to newest
	houses_popular = House.objects.order_by('-id')[:4]
	context = {
			'houses': houses,
			'houses_popular': houses_popular,
		}
	return render(request, 'papp/house.html', context)

def parking(request):
	if request.method == 'POST':
		city = request.POST.get('city')
		area_min = request.POST.get('area_min')
		area_max = request.POST.get('area_max')
		price_min = request.POST.get('price_min')
		price_max = request.POST.get('price_max')

		parkings = Parking.objects.filter(city=city, area__gte=area_min, 
			area__lte=area_max, price__gte=price_min, price__lte=price_max)
	else:
		parkings = Parking.objects.all().order_by('-id') # ordering from oldest to newest
	parkings_popular = Parking.objects.order_by('-id')[:4]
	context = {
			'parkings': parkings,
			'parkings_popular': parkings_popular,
		}
	return render(request, 'papp/parking.html', context)

def land(request):
	if request.method == 'POST':
		city = request.POST.get('city')
		area_min_land = request.POST.get('area_min_land')
		area_max_land = request.POST.get('area_max_land')
		price_min = request.POST.get('price_min')
		price_max = request.POST.get('price_max')
		purpose = request.POST.get('purpose')
		divisibility = request.POST.get('divisibility')

		lands = Land.objects.filter(city=city, area__gte=area_min_land, 
			area__lte=area_max_land, price__gte=price_min, price__lte=price_max,
			purpose=purpose, divisibility=divisibility)
	else:
		lands = Land.objects.all().order_by('-id') # ordering from oldest to newest
	lands_popular = Land.objects.order_by('-id')[:4]
	context = {
			'lands': lands,
			'lands_popular': lands_popular,
		}
	return render(request, 'papp/land.html', context)

def commercial(request):
	if request.method == 'POST':
		city = request.POST.get('city')
		area_min_commercial = request.POST.get('area_min_commercial')
		area_max_commercial = request.POST.get('area_max_commercial')
		price_min = request.POST.get('price_min')
		price_max = request.POST.get('price_max')

		commercials = Commercial.objects.filter(city=city, area__gte=area_min_commercial, 
			area__lte=area_max_commercial, price__gte=price_min, price__lte=price_max)
	else:
		commercials = Commercial.objects.all().order_by('-id') # ordering from oldest to newest
	commercials_popular = Commercial.objects.order_by('-id')[:4]
	context = {
			'commercials': commercials,
			'commercials_popular': commercials_popular,
		}
	return render(request, 'papp/commercial.html', context)

def industry(request):
	if request.method == 'POST':
		city = request.POST.get('city')
		area_min_industry = request.POST.get('area_min_industry')
		area_max_industry = request.POST.get('area_max_industry')
		price_min = request.POST.get('price_min')
		price_max = request.POST.get('price_max')

		industrys = Industry.objects.filter(city=city, area__gte=area_min_industry, 
			area__lte=area_max_industry, price__gte=price_min, price__lte=price_max)
	else:
		industrys = Industry.objects.all().order_by('-id') # ordering from oldest to newest
	industrys_popular = Industry.objects.order_by('-id')[:4]
	context = {
			'industrys': industrys,
			'industrys_popular': industrys_popular,
		}
	return render(request, 'papp/industry.html', context)

def auto(request):
	if request.method == 'POST':
		city = request.POST.get('city')
		color = request.POST.get('color')
		price_min = request.POST.get('price_min')
		price_max = request.POST.get('price_max')
		manufYear = request.POST.get('manufYear')
		transmission = request.POST.get('transmission')

		autos = Auto.objects.filter(city=city, price__gte=price_min, price__lte=price_max,
											manufYear=manufYear, transmission=transmission)
	else:
		autos = Auto.objects.all().order_by('-id') # ordering from oldest to newest
	autos_popular = Auto.objects.order_by('-id')[:4]
	context = {
			'autos': autos,
			'autos_popular': autos_popular,
		}
	return render(request, 'papp/auto.html', context)

def equipment(request):
	if request.method == 'POST':
		city = request.POST.get('city')
		color = request.POST.get('color')
		price_min = request.POST.get('price_min')
		price_max = request.POST.get('price_max')
		manufYear = request.POST.get('manufYear')

		equipments = Equipment.objects.filter(city=city, price__gte=price_min, color=color,
			price__lte=price_max, manufYear=manufYear)
	else:
		equipments = Equipment.objects.all().order_by('-id') # ordering from oldest to newest
	equipments_popular = Equipment.objects.order_by('-id')[:4]
	context = {
			'equipments': equipments,
			'equipments_popular': equipments_popular,
		}
	return render(request, 'papp/equipment.html', context)

def detail_flat(request, flat_id):
	# Вытаскиваем id предыдущего объекта
	try:
		previous_flat = Flat.objects.filter(pk__lt=flat_id).last()
	except IndexError:
		previous_flat = None
	# Вытаскиваем id следующего объекта
	try:
		next_flat = Flat.objects.filter(pk__gt=flat_id).first()
	except IndexError:
		next_flat = None
	# Вытаскиваем данные текущего объекта
	try:
		selected_flat = Flat.objects.get(pk=flat_id)
	except Flat.DoesNotExist:
		raise Http404("Ничего не найдено")
	# Пакуем всё в один контейнер и отправляем на страницу
	context = {
		'selected_flat': selected_flat,
		'previous_flat': previous_flat,
		'next_flat': next_flat,
	}
	return render(request, 'papp/detail_flat.html', context)

def detail_house(request, house_id):
	# Вытаскиваем id предыдущего объекта
	try:
		previous_house = House.objects.filter(pk__lt=house_id).last()
	except IndexError:
		previous_house = None
	# Вытаскиваем id следующего объекта
	try:
		next_house = House.objects.filter(pk__gt=house_id).first()
	except IndexError:
		next_house = None
	# Вытаскиваем данные текущего объекта
	try:
		selected_house = House.objects.get(pk=house_id)
	except House.DoesNotExist:
		raise Http404("Ничего не найдено")
	# Пакуем всё в один контейнер и отправляем на страницу
	context = {
		'selected_house': selected_house,
		'previous_house': previous_house,
		'next_house': next_house,
	}
	return render(request, 'papp/detail_house.html', context)

def detail_parking(request, parking_id):
	# Вытаскиваем id предыдущего объекта
	try:
		previous_parking = Parking.objects.filter(pk__lt=parking_id).last()
	except IndexError:
		previous_parking = None
	# Вытаскиваем id следующего объекта
	try:
		next_parking = Parking.objects.filter(pk__gt=parking_id).first()
	except IndexError:
		next_parking = None
	# Вытаскиваем данные текущего объекта
	try:
		selected_parking = Parking.objects.get(pk=parking_id)
	except Parking.DoesNotExist:
		raise Http404("Ничего не найдено")
	# Пакуем всё в один контейнер и отправляем на страницу
	context = {
		'selected_parking': selected_parking,
		'previous_parking': previous_parking,
		'next_parking': next_parking,
	}
	return render(request, 'papp/detail_parking.html', context)

def detail_land(request, land_id):
	# Вытаскиваем id предыдущего объекта
	try:
		previous_land = Land.objects.filter(pk__lt=land_id).last()
	except IndexError:
		previous_land = None
	# Вытаскиваем id следующего объекта
	try:
		next_land = Land.objects.filter(pk__gt=land_id).first()
	except IndexError:
		next_land = None
	# Вытаскиваем данные текущего объекта
	try:
		selected_land = Land.objects.get(pk=land_id)
	except Land.DoesNotExist:
		raise Http404("Ничего не найдено")
	# Пакуем всё в один контейнер и отправляем на страницу
	context = {
		'selected_land': selected_land,
		'previous_land': previous_land,
		'next_land': next_land,
	}
	return render(request, 'papp/detail_land.html', context)

def detail_commercial(request, commercial_id):
	# Вытаскиваем id предыдущего объекта
	try:
		previous_commercial = Commercial.objects.filter(pk__lt=commercial_id).last()
	except IndexError:
		previous_commercial = None
	# Вытаскиваем id следующего объекта
	try:
		next_commercial = Commercial.objects.filter(pk__gt=commercial_id).first()
	except IndexError:
		next_commercial = None
	# Вытаскиваем данные текущего объекта
	try:
		selected_commercial = Commercial.objects.get(pk=commercial_id)
	except Commercial.DoesNotExist:
		raise Http404("Ничего не найдено")
	# Пакуем всё в один контейнер и отправляем на страницу
	context = {
		'selected_commercial': selected_commercial,
		'previous_commercial': previous_commercial,
		'next_commercial': next_commercial,
	}
	return render(request, 'papp/detail_commercial.html', context)

def detail_industry(request, industry_id):
	# Вытаскиваем id предыдущего объекта
	try:
		previous_industry = Industry.objects.filter(pk__lt=industry_id).last()
	except IndexError:
		previous_industry = None
	# Вытаскиваем id следующего объекта
	try:
		next_industry = Industry.objects.filter(pk__gt=industry_id).first()
	except IndexError:
		next_industry = None
	# Вытаскиваем данные текущего объекта
	try:
		selected_industry = Industry.objects.get(pk=industry_id)
	except Industry.DoesNotExist:
		raise Http404("Ничего не найдено")
	# Пакуем всё в один контейнер и отправляем на страницу
	context = {
		'selected_industry': selected_industry,
		'previous_industry': previous_industry,
		'next_industry': next_industry,
	}
	return render(request, 'papp/detail_industry.html', context)

def detail_auto(request, auto_id):
	# Вытаскиваем id предыдущего объекта
	try:
		previous_auto = Auto.objects.filter(pk__lt=auto_id).last()
	except IndexError:
		previous_auto = None
	# Вытаскиваем id следующего объекта
	try:
		next_auto = Auto.objects.filter(pk__gt=auto_id).first()
	except IndexError:
		next_auto = None
	# Вытаскиваем данные текущего объекта
	try:
		selected_auto = Auto.objects.get(pk=auto_id)
	except Auto.DoesNotExist:
		raise Http404("Ничего не найдено")
	# Пакуем всё в один контейнер и отправляем на страницу
	context = {
		'selected_auto': selected_auto,
		'previous_auto': previous_auto,
		'next_auto': next_auto,
	}
	return render(request, 'papp/detail_auto.html', context)

def detail_equipment(request, equipment_id):
	# Вытаскиваем id предыдущего объекта
	try:
		previous_equipment = Equipment.objects.filter(pk__lt=equipment_id).last()
	except IndexError:
		previous_equipment = None
	# Вытаскиваем id следующего объекта
	try:
		next_equipment = Equipment.objects.filter(pk__gt=equipment_id).first()
	except IndexError:
		next_equipment = None
	# Вытаскиваем данные текущего объекта
	try:
		selected_equipment = Equipment.objects.get(pk=equipment_id)
	except Equipment.DoesNotExist:
		raise Http404("Ничего не найдено")
	# Пакуем всё в один контейнер и отправляем на страницу
	context = {
		'selected_equipment': selected_equipment,
		'previous_equipment': previous_equipment,
		'next_equipment': next_equipment,
	}
	return render(request, 'papp/detail_equipment.html', context)

def send_flat_view(request):
	if request.method == 'POST':
		name = request.user.first_name
		email = request.user.username
		phone = request.user.last_name
		property_id = request.POST.get('property_id')
		suggested_price = request.POST.get('suggested_price')
		send_mail(
	    	U'Поступила новая заявка от' + name,

	    	U'Фамилия, имя: ' + name + ' ' + 
	    	U'Email: ' + email + ' ' + 
	    	U'Номер телефона: ' + phone + ' ' + 
	    	U'Ссылка на объект: ' + '127.0.0.1:8000/detail_flat/' + property_id + '/',

	    	'darmesh.aidar@gmail.com',
	    	['danatsoy@gmail.com'],
	    	fail_silently=False,
		)
		content_type = ContentType.objects.get_for_model(Flat)
		flat_order = FlatOrder(user=request.user, content_type=content_type, 
								object_id=property_id, suggested_price=suggested_price)
		flat_order.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def send_house_view(request):
	if request.method == 'POST':
		name = request.user.first_name
		email = request.user.username
		phone = request.user.last_name
		property_id = request.POST.get('property_id')
		suggested_price = request.POST.get('suggested_price')
		send_mail(
	    	U'Поступила новая заявка от' + name,

	    	U'Фамилия, имя: ' + name + ' ' + 
	    	U'Email: ' + email + ' ' + 
	    	U'Номер телефона: ' + phone + ' ' + 
	    	U'Ссылка на объект: ' + '127.0.0.1:8000/detail_house/' + property_id + '/',

	    	'darmesh.aidar@gmail.com',
	    	['danatsoy@gmail.com'],
	    	fail_silently=False,
		)
		content_type = ContentType.objects.get_for_model(House)
		house_order = HouseOrder(user=request.user, content_type=content_type, 
								object_id=property_id, suggested_price=suggested_price)
		house_order.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def send_parking_view(request):
	if request.method == 'POST':
		name = request.user.first_name
		email = request.user.username
		phone = request.user.last_name
		property_id = request.POST.get('property_id')
		suggested_price = request.POST.get('suggested_price')
		send_mail(
	    	U'Поступила новая заявка от' + name,

	    	U'Фамилия, имя: ' + name + ' ' + 
	    	U'Email: ' + email + ' ' + 
	    	U'Номер телефона: ' + phone + ' ' + 
	    	U'Ссылка на объект: ' + '127.0.0.1:8000/detail_parking/' + property_id + '/',

	    	'darmesh.aidar@gmail.com',
	    	['danatsoy@gmail.com'],
	    	fail_silently=False,
		)
		content_type = ContentType.objects.get_for_model(Parking)
		parking_order = ParkingOrder(user=request.user, content_type=content_type, 
								object_id=property_id, suggested_price=suggested_price)
		parking_order.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def send_land_view(request):
	if request.method == 'POST':
		name = request.user.first_name
		email = request.user.username
		phone = request.user.last_name
		property_id = request.POST.get('property_id')
		suggested_price = request.POST.get('suggested_price')
		send_mail(
	    	U'Поступила новая заявка от' + name,

	    	U'Фамилия, имя: ' + name + ' ' + 
	    	U'Email: ' + email + ' ' + 
	    	U'Номер телефона: ' + phone + ' ' + 
	    	U'Ссылка на объект: ' + '127.0.0.1:8000/detail_land/' + property_id + '/',

	    	'darmesh.aidar@gmail.com',
	    	['danatsoy@gmail.com'],
	    	fail_silently=False,
		)
		content_type = ContentType.objects.get_for_model(Land)
		land_order = LandOrder(user=request.user, content_type=content_type, 
								object_id=property_id, suggested_price=suggested_price)
		land_order.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def send_commercial_view(request):
	if request.method == 'POST':
		name = request.user.first_name
		email = request.user.username
		phone = request.user.last_name
		property_id = request.POST.get('property_id')
		suggested_price = request.POST.get('suggested_price')
		send_mail(
	    	U'Поступила новая заявка от' + name,

	    	U'Фамилия, имя: ' + name + ' ' + 
	    	U'Email: ' + email + ' ' + 
	    	U'Номер телефона: ' + phone + ' ' + 
	    	U'Ссылка на объект: ' + '127.0.0.1:8000/detail_commercial/' + property_id + '/',

	    	'darmesh.aidar@gmail.com',
	    	['danatsoy@gmail.com'],
	    	fail_silently=False,
		)
		content_type = ContentType.objects.get_for_model(Commercial)
		commercial_order = CommercialOrder(user=request.user, content_type=content_type, 
								object_id=property_id, suggested_price=suggested_price)
		commercial_order.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def send_industry_view(request):
	if request.method == 'POST':
		name = request.user.first_name
		email = request.user.username
		phone = request.user.last_name
		property_id = request.POST.get('property_id')
		suggested_price = request.POST.get('suggested_price')
		send_mail(
	    	U'Поступила новая заявка от' + name,

	    	U'Фамилия, имя: ' + name + ' ' + 
	    	U'Email: ' + email + ' ' + 
	    	U'Номер телефона: ' + phone + ' ' + 
	    	U'Ссылка на объект: ' + '127.0.0.1:8000/detail_industry/' + property_id + '/',

	    	'darmesh.aidar@gmail.com',
	    	['danatsoy@gmail.com'],
	    	fail_silently=False,
		)
		content_type = ContentType.objects.get_for_model(Industry)
		industry_order = IndustryOrder(user=request.user, content_type=content_type, 
								object_id=property_id, suggested_price=suggested_price)
		industry_order.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def send_auto_view(request):
	if request.method == 'POST':
		name = request.user.first_name
		email = request.user.username
		phone = request.user.last_name
		property_id = request.POST.get('property_id')
		suggested_price = request.POST.get('suggested_price')
		send_mail(
	    	U'Поступила новая заявка от' + name,

	    	U'Фамилия, имя: ' + name + ' ' + 
	    	U'Email: ' + email + ' ' + 
	    	U'Номер телефона: ' + phone + ' ' + 
	    	U'Ссылка на объект: ' + '127.0.0.1:8000/detail_auto/' + property_id + '/',

	    	'darmesh.aidar@gmail.com',
	    	['danatsoy@gmail.com'],
	    	fail_silently=False,
		)
		content_type = ContentType.objects.get_for_model(Auto)
		auto_order = AutoOrder(user=request.user, content_type=content_type, 
								object_id=property_id, suggested_price=suggested_price)
		auto_order.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def send_equipment_view(request):
	if request.method == 'POST':
		name = request.user.first_name
		email = request.user.username
		phone = request.user.last_name
		property_id = request.POST.get('property_id')
		suggested_price = request.POST.get('suggested_price')
		send_mail(
	    	U'Поступила новая заявка от' + name,

	    	U'Фамилия, имя: ' + name + ' ' + 
	    	U'Email: ' + email + ' ' + 
	    	U'Номер телефона: ' + phone + ' ' + 
	    	U'Ссылка на объект: ' + '127.0.0.1:8000/detail_equipment/' + property_id + '/',

	    	'darmesh.aidar@gmail.com',
	    	['danatsoy@gmail.com'],
	    	fail_silently=False,
		)
		content_type = ContentType.objects.get_for_model(Equipment)
		equipment_order = EquipmentOrder(user=request.user, content_type=content_type, 
								object_id=property_id, suggested_price=suggested_price)
		equipment_order.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_flat_order_view(request, flatorder_id):
	flatorder = FlatOrder.objects.filter(id=flatorder_id)
	flatorder.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_house_order_view(request, houseorder_id):
	houseorder = HouseOrder.objects.filter(id=houseorder_id)
	houseorder.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_parking_order_view(request, parkingorder_id):
	parkingorder = ParkingOrder.objects.filter(id=parkingorder_id)
	parkingorder.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_land_order_view(request, landorder_id):
	landorder = LandOrder.objects.filter(id=landorder_id)
	landorder.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_commercial_order_view(request, commercialorder_id):
	commercialorder = CommercialOrder.objects.filter(id=commercialorder_id)
	commercialorder.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_industry_order_view(request, industryorder_id):
	industryorder = IndustryOrder.objects.filter(id=industryorder_id)
	industryorder.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_auto_order_view(request, autoorder_id):
	autoorder = AutoOrder.objects.filter(id=autoorder_id)
	autoorder.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_equipment_order_view(request, equipmentorder_id):
	equipmentorder = EquipmentOrder.objects.filter(id=equipmentorder_id)
	equipmentorder.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Общие функции для всех моделей
def account(request):
	if request.user.is_active:
		update_title = 'РЕДАКТИРОВАТЬ'
		success = ''
		update_form = UpdateProfileForm(request.POST or None)
		if update_form.is_valid():
			first_name = update_form.cleaned_data.get('first_name')
			username = update_form.cleaned_data.get('username')
			last_name = update_form.cleaned_data.get('last_name')
			password = update_form.cleaned_data.get('password')
			user = request.user
			if first_name:
				user.first_name = first_name
				print first_name
			if username:
				user.username = username
				user.email = username
				print username
			if last_name:
				user.last_name = last_name
				print last_name
			if password:
				user.set_password(password)
				print password
			user.save()
			success = 'Профиль успешно обновлен!'
		flatorders = FlatOrder.objects.filter(user=request.user)
		houseorders = HouseOrder.objects.filter(user=request.user)
		parkingorders = ParkingOrder.objects.filter(user=request.user)
		landorders = LandOrder.objects.filter(user=request.user)
		commercialorders = CommercialOrder.objects.filter(user=request.user)
		industryorders = IndustryOrder.objects.filter(user=request.user)
		autoorders = AutoOrder.objects.filter(user=request.user)
		equipmentorders = EquipmentOrder.objects.filter(user=request.user)
		context = {
			'update_form': update_form,
			'update_title': update_title,
			'flatorders': flatorders,
			'houseorders': houseorders,
			'parkingorders': parkingorders,
			'landorders': landorders,
			'commercialorders': commercialorders,
			'industryorders': industryorders,
			'autoorders': autoorders,
			'equipmentorders': equipmentorders,
			'success': success,
		}
		return render(request, 'papp/account.html', context)
	else:
		raise Http404("Пройдите авторизацию прежде чем войти в личный кабинет.")

def login_view(request):
	redirect_to = request.GET.get('next')
	login_title = 'ВОЙТИ'
	login_form = UserLoginForm(request.POST or None)
	if login_form.is_valid():
		username = login_form.cleaned_data.get('username')
		password = login_form.cleaned_data.get('password')
		user = authenticate(username=username, password=password) 
		request.session['username'] = username
		login(request, user)
		return redirect(redirect_to)
	context = {
		'login_form': login_form,
		'login_title': login_title,
		'next': redirect_to,
	}
	return render(request, 'papp/login.html', context)

def register_view(request):
	redirect_to = request.GET.get('next')
	reg_title = 'ЗАРЕГИСТРИРОВАТЬСЯ'
	reg_form = UserRegisterForm(request.POST or None)
	if reg_form.is_valid():
		first_name = reg_form.cleaned_data.get('first_name')
		username = reg_form.cleaned_data.get('username')
		last_name = reg_form.cleaned_data.get('last_name')
		password = reg_form.cleaned_data.get('password')
		user = User.objects.create_user(username=username, email=username,
			password=password, first_name=first_name, last_name=last_name)
		new_user = authenticate(username=user.username, password=password)
		request.session['username'] = username
		login(request, new_user)
		return redirect(redirect_to)
	context = {
			'reg_title': reg_title,
			'reg_form': reg_form,
			'next': redirect_to,
		}
	return render(request, 'papp/register.html', context)

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def logout_within_account_view(request):
	logout(request)
	return redirect('/')