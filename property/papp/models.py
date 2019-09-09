# encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from geoposition.fields import GeopositionField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# -------------------------------------------- Flat модель -------------------------------------------- 
class Flat(models.Model):
	CITIES = (
		('Алматы', 'Алматы'),
		('Астана', 'Астана'),
		('Актау', 'Актау'),
		('Актобе', 'Актобе'),
		('Астана', 'Астана'),
		('Атырау', 'Атырау'),
		('Жезказган', 'Жезказган'),
		('Караганда', 'Караганда'),
		('Кокшетау', 'Кокшетау'),
		('Костанай', 'Костанай'),
		('Кызылорда', 'Кызылорда'),
		('Павлодар', 'Павлодар'),
		('Петропавловск', 'Петропавловск'),
		('Семей', 'Семей'),
		('Талдыкорган', 'Талдыкорган'),
		('Тараз', 'Тараз'),
		('Уральск', 'Уральск'),
		('Усть-Каменогорск', 'Усть-Каменогорск'),
		('Шымкент', 'Шымкент'),
	)

	ROOM_NUMBERS = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('5+', '5+'),
	)

	CONST_TYPES = (
		('Панельный', 'Панельный'),
		('Кирпичный', 'Кирпичный'),
		('Монолитный', 'Монолитный'),
	)

	city = models.CharField('Город', max_length=200, choices=CITIES)
	district = models.CharField('Район', max_length=200)
	roomNumber = models.CharField('Количество комнат', max_length=200, choices=ROOM_NUMBERS)
	price = models.BigIntegerField('Цена')
	constYear = models.IntegerField('Год постройки')
	storey = models.CharField('Этаж', max_length=200)
	area = models.FloatField('Площадь', blank = True, null = True)

	# additional info
	livingArea = models.FloatField('Жилая площадь', blank = True, null = True)
	storeyNumber = models.IntegerField('Количество этажей')
	constType = models.CharField('Тип строения', max_length=200, choices=CONST_TYPES)

	contacts = models.TextField('Контактные данные')
	contactFace = models.CharField('Контактное лицо', max_length=200)
	address = models.CharField('Адрес', max_length=400)
	description = models.TextField('Описание')
	image1 = models.FileField('Фото 1', null=True, blank=True)
	image2 = models.FileField('Фото 2', null=True, blank=True)
	image3 = models.FileField('Фото 3', null=True, blank=True)
	image4 = models.FileField('Фото 4', null=True, blank=True)
	image5 = models.FileField('Фото 5', null=True, blank=True)

	# geoposition
	position = GeopositionField('Позиция', blank=True)

	class Meta:
		verbose_name_plural='Квартиры'

	def __unicode__(self):
		return U"%s комнатная квартира, %s, %s"%(self.roomNumber, self.city, self.address)

	def save(self, *args, **kwargs):
	# delete old file when replacing by updating the file
		try:
			this = Flat.objects.get(id=self.id)
			if this.image1 != self.image1:
				this.image1.delete(save=False)
			if this.image2 != self.image2:
				this.image2.delete(save=False)
			if this.image3 != self.image3:
				this.image3.delete(save=False)
			if this.image4 != self.image4:
				this.image4.delete(save=False)
			if this.image5 != self.image5:
				this.image5.delete(save=False)
		except: pass # when new photo then we do nothing, normal case          
		super(Flat, self).save(*args, **kwargs)

@receiver(pre_delete, sender=Flat)
def flat_delete(sender, instance, **kwargs):
	instance.image1.delete(False)
	instance.image2.delete(False)
	instance.image3.delete(False)
	instance.image4.delete(False)
	instance.image5.delete(False)

# -------------------------------------------- FlatOrder модель -------------------------------------------- 
class FlatOrder(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	suggested_price = models.BigIntegerField('Предложенная цена, тг', null=True, blank=True)
	order_date = models.DateTimeField('Дата подачи заявки', auto_now_add=True)

	class Meta:
		verbose_name_plural='Заявки на квартиры'

	def __unicode__(self):
		return str(self.user.username)

	def __str__(self):
		return str(self.user.username)

# -------------------------------------------- House модель -------------------------------------------- 
class House(models.Model):
	CITIES = (
		('Алматы', 'Алматы'),
		('Астана', 'Астана'),
		('Актау', 'Актау'),
		('Актобе', 'Актобе'),
		('Астана', 'Астана'),
		('Атырау', 'Атырау'),
		('Жезказган', 'Жезказган'),
		('Караганда', 'Караганда'),
		('Кокшетау', 'Кокшетау'),
		('Костанай', 'Костанай'),
		('Кызылорда', 'Кызылорда'),
		('Павлодар', 'Павлодар'),
		('Петропавловск', 'Петропавловск'),
		('Семей', 'Семей'),
		('Талдыкорган', 'Талдыкорган'),
		('Тараз', 'Тараз'),
		('Уральск', 'Уральск'),
		('Усть-Каменогорск', 'Усть-Каменогорск'),
		('Шымкент', 'Шымкент'),
	)

	ROOM_NUMBERS = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('5+', '5+'),
	)

	city = models.CharField('Город', max_length=200, choices=CITIES)
	district = models.CharField('Район', max_length=200)
	roomNumber = models.CharField('Количество комнат', max_length=200, choices=ROOM_NUMBERS)
	price = models.BigIntegerField('Цена')
	constYear = models.IntegerField('Год постройки')
	storeyNumber = models.IntegerField('Этажей в доме')
	area = models.FloatField('Площадь', blank = True, null = True)

	# additional info
	livingArea = models.FloatField('Жилая площадь', blank = True, null = True)
	wallMaterial = models.CharField('Материал стен', max_length=200)
	windows = models.CharField('Окна', max_length=200)
	landArea = models.FloatField('Площадь земельного участка', blank = True, null = True)
	buildingArea = models.FloatField('Общая площадь строений', blank = True, null = True)
	footer = models.CharField('Подвал', max_length=200)
	gasSupply = models.CharField('Газоснабжение', max_length=200)
	sewerage = models.CharField('Канализация', max_length=200)
	waterSupply = models.CharField('Водоснабжение', max_length=200)
	powerSupply = models.CharField('Электроснабжение', max_length=200)

	contacts = models.TextField('Контактные данные')
	contactFace = models.CharField('Контактное лицо', max_length=200)
	address = models.CharField('Адрес', max_length=400)
	description = models.TextField('Описание')
	image1 = models.FileField('Фото 1', null=True, blank=True)
	image2 = models.FileField('Фото 2', null=True, blank=True)
	image3 = models.FileField('Фото 3', null=True, blank=True)
	image4 = models.FileField('Фото 4', null=True, blank=True)
	image5 = models.FileField('Фото 5', null=True, blank=True)

	# geoposition
	position = GeopositionField('Позиция', blank=True)

	class Meta:
		verbose_name_plural='Жилые дома'

	def __unicode__(self):
		return U"%s комнатный жилой дом, %s, %s"%(self.roomNumber, self.city, self.address)

	def save(self, *args, **kwargs):
	# delete old file when replacing by updating the file
		try:
			this = House.objects.get(id=self.id)
			if this.image1 != self.image1:
				this.image1.delete(save=False)
			if this.image2 != self.image2:
				this.image2.delete(save=False)
			if this.image3 != self.image3:
				this.image3.delete(save=False)
			if this.image4 != self.image4:
				this.image4.delete(save=False)
			if this.image5 != self.image5:
				this.image5.delete(save=False)
		except: pass # when new photo then we do nothing, normal case          
		super(House, self).save(*args, **kwargs)

@receiver(pre_delete, sender=House)
def house_delete(sender, instance, **kwargs):
	instance.image1.delete(False)
	instance.image2.delete(False)
	instance.image3.delete(False)
	instance.image4.delete(False)
	instance.image5.delete(False)

# -------------------------------------------- HouseOrder модель -------------------------------------------- 
class HouseOrder(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	suggested_price = models.BigIntegerField('Предложенная цена, тг', null=True, blank=True)
	order_date = models.DateTimeField('Дата подачи заявки', auto_now_add=True)

	class Meta:
		verbose_name_plural='Заявки на жилые дома'

	def __unicode__(self):
		return str(self.user.username)

	def __str__(self):
		return str(self.user.username)

# -------------------------------------------- Parking модель -------------------------------------------- 
class Parking(models.Model):
	CITIES = (
		('Алматы', 'Алматы'),
		('Астана', 'Астана'),
		('Актау', 'Актау'),
		('Актобе', 'Актобе'),
		('Астана', 'Астана'),
		('Атырау', 'Атырау'),
		('Жезказган', 'Жезказган'),
		('Караганда', 'Караганда'),
		('Кокшетау', 'Кокшетау'),
		('Костанай', 'Костанай'),
		('Кызылорда', 'Кызылорда'),
		('Павлодар', 'Павлодар'),
		('Петропавловск', 'Петропавловск'),
		('Семей', 'Семей'),
		('Талдыкорган', 'Талдыкорган'),
		('Тараз', 'Тараз'),
		('Уральск', 'Уральск'),
		('Усть-Каменогорск', 'Усть-Каменогорск'),
		('Шымкент', 'Шымкент'),
	)

	city = models.CharField('Город', max_length=200, choices=CITIES)
	district = models.CharField('Район', max_length=200)
	price = models.BigIntegerField('Цена')
	area = models.FloatField('Площадь', blank = True, null = True)

	# additional info
	height = models.FloatField('Высота', blank = True, null = True)
	level = models.CharField('Уровень', max_length=200)
	storey = models.CharField('Этаж', max_length=200)
	heated = models.CharField('Отапливаемый', max_length=200)
	constYear = models.IntegerField('Год постройки')
	safety = models.CharField('Безопасность', max_length=200)

	contacts = models.TextField('Контактные данные')
	contactFace = models.CharField('Контактное лицо', max_length=200)
	address = models.CharField('Адрес', max_length=400)
	description = models.TextField('Описание')
	image1 = models.FileField('Фото 1', null=True, blank=True)
	image2 = models.FileField('Фото 2', null=True, blank=True)
	image3 = models.FileField('Фото 3', null=True, blank=True)
	image4 = models.FileField('Фото 4', null=True, blank=True)
	image5 = models.FileField('Фото 5', null=True, blank=True)

	# geoposition
	position = GeopositionField('Позиция', blank=True)

	class Meta:
		verbose_name_plural='Паркинги'

	def __unicode__(self):
		return U"%s метровый паркинг на %s этаже, %s, %s"%(self.height, self.storey, self.city, self.address)

	def save(self, *args, **kwargs):
	# delete old file when replacing by updating the file
		try:
			this = House.objects.get(id=self.id)
			if this.image1 != self.image1:
				this.image1.delete(save=False)
			if this.image2 != self.image2:
				this.image2.delete(save=False)
			if this.image3 != self.image3:
				this.image3.delete(save=False)
			if this.image4 != self.image4:
				this.image4.delete(save=False)
			if this.image5 != self.image5:
				this.image5.delete(save=False)
		except: pass # when new photo then we do nothing, normal case          
		super(Parking, self).save(*args, **kwargs)

@receiver(pre_delete, sender=Parking)
def parking_delete(sender, instance, **kwargs):
	instance.image1.delete(False)
	instance.image2.delete(False)
	instance.image3.delete(False)
	instance.image4.delete(False)
	instance.image5.delete(False)

# -------------------------------------------- ParkingOrder модель -------------------------------------------- 
class ParkingOrder(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	suggested_price = models.BigIntegerField('Предложенная цена, тг', null=True, blank=True)
	order_date = models.DateTimeField('Дата подачи заявки', auto_now_add=True)

	class Meta:
		verbose_name_plural='Заявки на паркинги'

	def __unicode__(self):
		return str(self.user.username)

	def __str__(self):
		return str(self.user.username)

# -------------------------------------------- Land модель -------------------------------------------- 
class Land(models.Model):
	CITIES = (
		('Алматы', 'Алматы'),
		('Астана', 'Астана'),
		('Актау', 'Актау'),
		('Актобе', 'Актобе'),
		('Астана', 'Астана'),
		('Атырау', 'Атырау'),
		('Жезказган', 'Жезказган'),
		('Караганда', 'Караганда'),
		('Кокшетау', 'Кокшетау'),
		('Костанай', 'Костанай'),
		('Кызылорда', 'Кызылорда'),
		('Павлодар', 'Павлодар'),
		('Петропавловск', 'Петропавловск'),
		('Семей', 'Семей'),
		('Талдыкорган', 'Талдыкорган'),
		('Тараз', 'Тараз'),
		('Уральск', 'Уральск'),
		('Усть-Каменогорск', 'Усть-Каменогорск'),
		('Шымкент', 'Шымкент'),
	)

	PURPOSE = (
		('Для размещения производственной базы', 'Для размещения производственной базы'),
		('Для ведения товарно-сельского хозяйства', 'Для ведения товарно-сельского хозяйства'),
		('Для ведения крестьянского хозяйства', 'Для ведения крестьянского хозяйства'),
		('ЛПХ', 'ЛПХ'),
		('ИЖС', 'ИЖС'),
		('КХ', 'КХ'),
		('СТ', 'СТ'),
		('Для эксплуатации и обслуживания автостоянки легковых автомобилей', 
			'Для эксплуатации и обслуживания автостоянки легковых автомобилей'),
		('Для эксплуатации и обслуживания гостиницы', 'Для эксплуатации и обслуживания гостиницы'),
		('Для эксплуатации и обслуживания производственной базы', 
			'Для эксплуатации и обслуживания производственной базы'),
		('Ведение крестьянского хозяйства', 'Ведение крестьянского хозяйства'),
	)

	DIVISIBILITY = (
		('Делимый', 'Делимый'),
		('Неделимый', 'Неделимый'),
	)

	city = models.CharField('Город', max_length=200, choices=CITIES)
	district = models.CharField('Район', max_length=200)
	purpose = models.CharField('Целевое назначение', max_length=400, choices=PURPOSE)
	divisibility = models.CharField('Делимость', max_length=200, choices=DIVISIBILITY)
	price = models.BigIntegerField('Цена')
	area = models.FloatField('Площадь', blank = True, null = True)

	# additional info
	landType = models.CharField('Тип участка', max_length=200)
	rented = models.CharField('В аренде', max_length=200)
	communications = models.CharField('Коммуникации', max_length=200)

	contacts = models.TextField('Контактные данные')
	contactFace = models.CharField('Контактное лицо', max_length=200)
	address = models.CharField('Адрес', max_length=400)
	description = models.TextField('Описание')
	image1 = models.FileField('Фото 1', null=True, blank=True)
	image2 = models.FileField('Фото 2', null=True, blank=True)
	image3 = models.FileField('Фото 3', null=True, blank=True)
	image4 = models.FileField('Фото 4', null=True, blank=True)
	image5 = models.FileField('Фото 5', null=True, blank=True)

	# geoposition
	position = GeopositionField('Позиция', blank=True)

	class Meta:
		verbose_name_plural='Земельные участки'

	def __unicode__(self):
		return U"Земельный участок, %s, %s"%(self.city, self.address)

	def save(self, *args, **kwargs):
	# delete old file when replacing by updating the file
		try:
			this = Land.objects.get(id=self.id)
			if this.image1 != self.image1:
				this.image1.delete(save=False)
			if this.image2 != self.image2:
				this.image2.delete(save=False)
			if this.image3 != self.image3:
				this.image3.delete(save=False)
			if this.image4 != self.image4:
				this.image4.delete(save=False)
			if this.image5 != self.image5:
				this.image5.delete(save=False)
		except: pass # when new photo then we do nothing, normal case          
		super(Land, self).save(*args, **kwargs)

@receiver(pre_delete, sender=Land)
def land_delete(sender, instance, **kwargs):
	instance.image1.delete(False)
	instance.image2.delete(False)
	instance.image3.delete(False)
	instance.image4.delete(False)
	instance.image5.delete(False)

# -------------------------------------------- LandOrder модель -------------------------------------------- 
class LandOrder(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	suggested_price = models.BigIntegerField('Предложенная цена, тг', null=True, blank=True)
	order_date = models.DateTimeField('Дата подачи заявки', auto_now_add=True)

	class Meta:
		verbose_name_plural='Заявки на земельные участки'

	def __unicode__(self):
		return str(self.user.username)

	def __str__(self):
		return str(self.user.username)

# -------------------------------------------- Commercial модель -------------------------------------------- 
class Commercial(models.Model):
	CITIES = (
		('Алматы', 'Алматы'),
		('Астана', 'Астана'),
		('Актау', 'Актау'),
		('Актобе', 'Актобе'),
		('Астана', 'Астана'),
		('Атырау', 'Атырау'),
		('Жезказган', 'Жезказган'),
		('Караганда', 'Караганда'),
		('Кокшетау', 'Кокшетау'),
		('Костанай', 'Костанай'),
		('Кызылорда', 'Кызылорда'),
		('Павлодар', 'Павлодар'),
		('Петропавловск', 'Петропавловск'),
		('Семей', 'Семей'),
		('Талдыкорган', 'Талдыкорган'),
		('Тараз', 'Тараз'),
		('Уральск', 'Уральск'),
		('Усть-Каменогорск', 'Усть-Каменогорск'),
		('Шымкент', 'Шымкент'),
	)

	city = models.CharField('Город', max_length=200, choices=CITIES)
	district = models.CharField('Район', max_length=200)
	price = models.BigIntegerField('Цена')
	area = models.FloatField('Площадь', blank = True, null = True)

	# additional info
	storey = models.CharField('Этаж', max_length=200)
	areaUseful = models.FloatField('Полезная площадь', blank = True, null = True)
	constYear = models.IntegerField('Год постройки')
	wallMaterial = models.CharField('Материал стен', max_length=200)
	floor = models.CharField('Полы', max_length=200)
	hotwaterSupply = models.CharField('Горячее водоснабжение', max_length=200)
	waterSupply = models.CharField('Водоснабжение', max_length=200)
	sewerage = models.CharField('Канализация', max_length=200)
	powerSupply = models.CharField('Электроснабжение', max_length=200)
	heating = models.CharField('Отопление', max_length=200)
	phone = models.CharField('Телефон', max_length=200)
	internet = models.CharField('Интернет', max_length=200)
	safety = models.CharField('Безопасность', max_length=200)
	footer = models.CharField('Подвал', max_length=200)
	purpose = models.CharField('Целевое назначение', max_length=200)

	contacts = models.TextField('Контактные данные')
	contactFace = models.CharField('Контактное лицо', max_length=200)
	address = models.CharField('Адрес', max_length=400)
	description = models.TextField('Описание')
	image1 = models.FileField('Фото 1', null=True, blank=True)
	image2 = models.FileField('Фото 2', null=True, blank=True)
	image3 = models.FileField('Фото 3', null=True, blank=True)
	image4 = models.FileField('Фото 4', null=True, blank=True)
	image5 = models.FileField('Фото 5', null=True, blank=True)

	# geoposition
	position = GeopositionField('Позиция', blank=True)

	class Meta:
		verbose_name_plural='Коммерческая'

	def __unicode__(self):
		return U"Коммерческий объект, %s, %s"%(self.city, self.address)

	def save(self, *args, **kwargs):
	# delete old file when replacing by updating the file
		try:
			this = Commercial.objects.get(id=self.id)
			if this.image1 != self.image1:
				this.image1.delete(save=False)
			if this.image2 != self.image2:
				this.image2.delete(save=False)
			if this.image3 != self.image3:
				this.image3.delete(save=False)
			if this.image4 != self.image4:
				this.image4.delete(save=False)
			if this.image5 != self.image5:
				this.image5.delete(save=False)
		except: pass # when new photo then we do nothing, normal case          
		super(Commercial, self).save(*args, **kwargs)

@receiver(pre_delete, sender=Commercial)
def commercial_delete(sender, instance, **kwargs):
	instance.image1.delete(False)
	instance.image2.delete(False)
	instance.image3.delete(False)
	instance.image4.delete(False)
	instance.image5.delete(False)

# -------------------------------------------- ParkingOrder модель -------------------------------------------- 
class CommercialOrder(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	suggested_price = models.BigIntegerField('Предложенная цена, тг', null=True, blank=True)
	order_date = models.DateTimeField('Дата подачи заявки', auto_now_add=True)

	class Meta:
		verbose_name_plural='Заявки на коммерческие'

	def __unicode__(self):
		return str(self.user.username)

	def __str__(self):
		return str(self.user.username)

# -------------------------------------------- Industry модель -------------------------------------------- 
class Industry(models.Model):
	CITIES = (
		('Алматы', 'Алматы'),
		('Астана', 'Астана'),
		('Актау', 'Актау'),
		('Актобе', 'Актобе'),
		('Астана', 'Астана'),
		('Атырау', 'Атырау'),
		('Жезказган', 'Жезказган'),
		('Караганда', 'Караганда'),
		('Кокшетау', 'Кокшетау'),
		('Костанай', 'Костанай'),
		('Кызылорда', 'Кызылорда'),
		('Павлодар', 'Павлодар'),
		('Петропавловск', 'Петропавловск'),
		('Семей', 'Семей'),
		('Талдыкорган', 'Талдыкорган'),
		('Тараз', 'Тараз'),
		('Уральск', 'Уральск'),
		('Усть-Каменогорск', 'Усть-Каменогорск'),
		('Шымкент', 'Шымкент'),
	)

	city = models.CharField('Город', max_length=200, choices=CITIES)
	district = models.CharField('Район', max_length=200)
	deadlockExistence = models.CharField('Наличие ж/д тупика', max_length=200)
	price = models.BigIntegerField('Цена')
	area = models.FloatField('Площадь', blank = True, null = True)

	# additional info
	industryType = models.CharField('Тип базы (по назначению)', max_length=200)
	purpose = models.CharField('Целевое назначение', max_length=200)
	constYear = models.IntegerField('Год постройки')
	constMaterial = models.CharField('Материал зданий', max_length=200)
	areaLand = models.FloatField('Площадь земельного участка', blank = True, null = True)
	purposeLand = models.CharField('Назначение земельного участка', max_length=200)
	divisibilityLand = models.CharField('Делимость земельного участка', max_length=200)
	gasSupply = models.CharField('Газоснабжение', max_length=200)
	sewerage = models.CharField('Канализация', max_length=200)
	waterSupply = models.CharField('Водоснабжение', max_length=200)
	powerSupply = models.CharField('Электроснабжение', max_length=200)
	heating = models.CharField('Отопление', max_length=200)
	phone = models.CharField('Телефон', max_length=200)
	safety = models.CharField('Безопасность', max_length=200)

	contacts = models.TextField('Контактные данные')
	contactFace = models.CharField('Контактное лицо', max_length=200)
	address = models.CharField('Адрес', max_length=400)
	description = models.TextField('Описание')
	image1 = models.FileField('Фото 1', null=True, blank=True)
	image2 = models.FileField('Фото 2', null=True, blank=True)
	image3 = models.FileField('Фото 3', null=True, blank=True)
	image4 = models.FileField('Фото 4', null=True, blank=True)
	image5 = models.FileField('Фото 5', null=True, blank=True)

	# geoposition
	position = GeopositionField('Позиция', blank=True)

	class Meta:
		verbose_name_plural='Промбаза'

	def __unicode__(self):
		return U"Промышленная база, %s, %s"%(self.city, self.address)

	def save(self, *args, **kwargs):
	# delete old file when replacing by updating the file
		try:
			this = Industry.objects.get(id=self.id)
			if this.image1 != self.image1:
				this.image1.delete(save=False)
			if this.image2 != self.image2:
				this.image2.delete(save=False)
			if this.image3 != self.image3:
				this.image3.delete(save=False)
			if this.image4 != self.image4:
				this.image4.delete(save=False)
			if this.image5 != self.image5:
				this.image5.delete(save=False)
		except: pass # when new photo then we do nothing, normal case          
		super(Industry, self).save(*args, **kwargs)

@receiver(pre_delete, sender=Industry)
def industry_delete(sender, instance, **kwargs):
	instance.image1.delete(False)
	instance.image2.delete(False)
	instance.image3.delete(False)
	instance.image4.delete(False)
	instance.image5.delete(False)

# -------------------------------------------- IndustryOrder модель -------------------------------------------- 
class IndustryOrder(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	suggested_price = models.BigIntegerField('Предложенная цена, тг', null=True, blank=True)
	order_date = models.DateTimeField('Дата подачи заявки', auto_now_add=True)

	class Meta:
		verbose_name_plural='Заявки на промбазы'

	def __unicode__(self):
		return str(self.user.username)

	def __str__(self):
		return str(self.user.username)

# -------------------------------------------- Auto модель -------------------------------------------- 
class Auto(models.Model):
	CITIES = (
		('Алматы', 'Алматы'),
		('Астана', 'Астана'),
		('Актау', 'Актау'),
		('Актобе', 'Актобе'),
		('Астана', 'Астана'),
		('Атырау', 'Атырау'),
		('Жезказган', 'Жезказган'),
		('Караганда', 'Караганда'),
		('Кокшетау', 'Кокшетау'),
		('Костанай', 'Костанай'),
		('Кызылорда', 'Кызылорда'),
		('Павлодар', 'Павлодар'),
		('Петропавловск', 'Петропавловск'),
		('Семей', 'Семей'),
		('Талдыкорган', 'Талдыкорган'),
		('Тараз', 'Тараз'),
		('Уральск', 'Уральск'),
		('Усть-Каменогорск', 'Усть-Каменогорск'),
		('Шымкент', 'Шымкент'),
	)

	COLORS = (
		('бронза', 'бронза'),
		('вишня', 'вишня'),
		('хамелеон', 'хамелеон'),
		('бежевый', 'бежевый'),
		('белый', 'белый'),
		('бирюзовый', 'бирюзовый'),
		('бордовый', 'бордовый'),
		('голубой', 'голубой'),
		('жёлтый', 'жёлтый'),
		('зелёный', 'зелёный'),
		('золотистый', 'золотистый'),
		('коричневый', 'коричневый'),
		('красный', 'красный'),
		('оранжевый', 'оранжевый'),
		('розовый', 'розовый'),
		('серебристый', 'серебристый'),
		('серый', 'серый'),
		('синий', 'синий'),
		('сиреневый', 'сиреневый'),
		('фиолетовый', 'фиолетовый'),
		('чёрный', 'чёрный'),
	)

	TRANSMISSIONS = (
		('механика', 'механика'),
		('автомат', 'автомат'),
		('типтроник', 'типтроник'),
		('вариатор', 'вариатор'),
	)

	city = models.CharField('Город', max_length=200, choices=CITIES)
	color = models.CharField('Цвет', max_length=200, choices=COLORS)
	price = models.BigIntegerField('Цена')
	manufYear = models.IntegerField('Год выпуска', blank = True, null = True)
	transmission = models.CharField('КПП', max_length=200, choices=TRANSMISSIONS)

	# additional info
	brand = models.CharField('Марка', max_length=200)
	model = models.CharField('Модель', max_length=200)
	engineCapacity = models.FloatField('Объём двигателя', blank = True, null = True)
	autoType = models.CharField('Тип авто', max_length=200)
	status = models.CharField('Состояние', max_length=200)
	body = models.CharField('Кузов', max_length=200)

	contacts = models.TextField('Контактные данные')
	contactFace = models.CharField('Контактное лицо', max_length=200)
	description = models.TextField('Описание')
	image1 = models.FileField('Фото 1', null=True, blank=True)
	image2 = models.FileField('Фото 2', null=True, blank=True)
	image3 = models.FileField('Фото 3', null=True, blank=True)
	image4 = models.FileField('Фото 4', null=True, blank=True)
	image5 = models.FileField('Фото 5', null=True, blank=True)

	class Meta:
		verbose_name_plural='Авто'

	def __unicode__(self):
		return U"%s %s"%(self.brand, self.model)

	def save(self, *args, **kwargs):
	# delete old file when replacing by updating the file
		try:
			this = Auto.objects.get(id=self.id)
			if this.image1 != self.image1:
				this.image1.delete(save=False)
			if this.image2 != self.image2:
				this.image2.delete(save=False)
			if this.image3 != self.image3:
				this.image3.delete(save=False)
			if this.image4 != self.image4:
				this.image4.delete(save=False)
			if this.image5 != self.image5:
				this.image5.delete(save=False)
		except: pass # when new photo then we do nothing, normal case          
		super(Auto, self).save(*args, **kwargs)

@receiver(pre_delete, sender=Auto)
def auto_delete(sender, instance, **kwargs):
	instance.image1.delete(False)
	instance.image2.delete(False)
	instance.image3.delete(False)
	instance.image4.delete(False)
	instance.image5.delete(False)

# -------------------------------------------- AutoOrder модель -------------------------------------------- 
class AutoOrder(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	suggested_price = models.BigIntegerField('Предложенная цена, тг', null=True, blank=True)
	order_date = models.DateTimeField('Дата подачи заявки', auto_now_add=True)

	class Meta:
		verbose_name_plural='Заявки на авто'

	def __unicode__(self):
		return str(self.user.username)

	def __str__(self):
		return str(self.user.username)

# -------------------------------------------- Equipment модель -------------------------------------------- 
class Equipment(models.Model):
	CITIES = (
		('Алматы', 'Алматы'),
		('Астана', 'Астана'),
		('Актау', 'Актау'),
		('Актобе', 'Актобе'),
		('Астана', 'Астана'),
		('Атырау', 'Атырау'),
		('Жезказган', 'Жезказган'),
		('Караганда', 'Караганда'),
		('Кокшетау', 'Кокшетау'),
		('Костанай', 'Костанай'),
		('Кызылорда', 'Кызылорда'),
		('Павлодар', 'Павлодар'),
		('Петропавловск', 'Петропавловск'),
		('Семей', 'Семей'),
		('Талдыкорган', 'Талдыкорган'),
		('Тараз', 'Тараз'),
		('Уральск', 'Уральск'),
		('Усть-Каменогорск', 'Усть-Каменогорск'),
		('Шымкент', 'Шымкент'),
	)

	COLORS = (
		('бронза', 'бронза'),
		('вишня', 'вишня'),
		('хамелеон', 'хамелеон'),
		('бежевый', 'бежевый'),
		('белый', 'белый'),
		('бирюзовый', 'бирюзовый'),
		('бордовый', 'бордовый'),
		('голубой', 'голубой'),
		('жёлтый', 'жёлтый'),
		('зелёный', 'зелёный'),
		('золотистый', 'золотистый'),
		('коричневый', 'коричневый'),
		('красный', 'красный'),
		('оранжевый', 'оранжевый'),
		('розовый', 'розовый'),
		('серебристый', 'серебристый'),
		('серый', 'серый'),
		('синий', 'синий'),
		('сиреневый', 'сиреневый'),
		('фиолетовый', 'фиолетовый'),
		('чёрный', 'чёрный'),
	)

	city = models.CharField('Город', max_length=200, choices=CITIES)
	color = models.CharField('Цвет', max_length=200, choices=COLORS)
	price = models.BigIntegerField('Цена')
	manufYear = models.IntegerField('Год выпуска', blank = True, null = True)

	# additional info
	brand = models.CharField('Марка', max_length=200)
	equipmentType = models.CharField('Тип техники', max_length=200)
	fuelType = models.CharField('Тип топлива', max_length=200)

	contacts = models.TextField('Контактные данные')
	contactFace = models.CharField('Контактное лицо', max_length=200)
	description = models.TextField('Описание')
	image1 = models.FileField('Фото 1', null=True, blank=True)
	image2 = models.FileField('Фото 2', null=True, blank=True)
	image3 = models.FileField('Фото 3', null=True, blank=True)
	image4 = models.FileField('Фото 4', null=True, blank=True)
	image5 = models.FileField('Фото 5', null=True, blank=True)

	class Meta:
		verbose_name_plural='Спецтехника'

	def __unicode__(self):
		return U"%s"%(self.brand)

	def save(self, *args, **kwargs):
	# delete old file when replacing by updating the file
		try:
			this = Equipment.objects.get(id=self.id)
			if this.image1 != self.image1:
				this.image1.delete(save=False)
			if this.image2 != self.image2:
				this.image2.delete(save=False)
			if this.image3 != self.image3:
				this.image3.delete(save=False)
			if this.image4 != self.image4:
				this.image4.delete(save=False)
			if this.image5 != self.image5:
				this.image5.delete(save=False)
		except: pass # when new photo then we do nothing, normal case          
		super(Equipment, self).save(*args, **kwargs)

@receiver(pre_delete, sender=Auto)
def equipment_delete(sender, instance, **kwargs):
	instance.image1.delete(False)
	instance.image2.delete(False)
	instance.image3.delete(False)
	instance.image4.delete(False)
	instance.image5.delete(False)

# -------------------------------------------- EquipmentOrder модель -------------------------------------------- 
class EquipmentOrder(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	suggested_price = models.BigIntegerField('Предложенная цена, тг', null=True, blank=True)
	order_date = models.DateTimeField('Дата подачи заявки', auto_now_add=True)

	class Meta:
		verbose_name_plural='Заявки на спецтехнику'

	def __unicode__(self):
		return str(self.user.username)

	def __str__(self):
		return str(self.user.username)