# encoding: utf-8
from django.contrib import admin
from .models import Flat, FlatOrder, House, HouseOrder, Parking, ParkingOrder
from .models import Land, LandOrder, Commercial, CommercialOrder, Industry, IndustryOrder
from .models import Auto, AutoOrder, Equipment, EquipmentOrder

# -------------------------------------------- Flat часть -------------------------------------------- 
class FlatAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	list_filter = ['city', 'district', 'roomNumber', 'storey']
	search_fields = ['address', 'description']
	class Meta:
		model = Flat

class FlatOrderAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'content_object', 'suggested_price', 'order_date']
	class Meta:
		model = Flat

admin.site.register(Flat, FlatAdmin)
admin.site.register(FlatOrder, FlatOrderAdmin)

# -------------------------------------------- House часть -------------------------------------------- 
class HouseAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	list_filter = ['city', 'district', 'roomNumber', 'storeyNumber']
	search_fields = ['address', 'description']
	class Meta:
		model = House

class HouseOrderAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'content_object', 'suggested_price', 'order_date']
	class Meta:
		model = House

admin.site.register(House, HouseAdmin)
admin.site.register(HouseOrder, HouseOrderAdmin)

# -------------------------------------------- Parking часть -------------------------------------------- 
class ParkingAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	list_filter = ['city', 'district']
	search_fields = ['address', 'description']
	class Meta:
		model = Parking

class ParkingOrderAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'content_object', 'suggested_price', 'order_date']
	class Meta:
		model = Parking

admin.site.register(Parking, ParkingAdmin)
admin.site.register(ParkingOrder, ParkingOrderAdmin)

# -------------------------------------------- Land часть -------------------------------------------- 
class LandAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	list_filter = ['city', 'district']
	search_fields = ['address', 'description']
	class Meta:
		model = Land

class LandOrderAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'content_object', 'suggested_price', 'order_date']
	class Meta:
		model = Land

admin.site.register(Land, LandAdmin)
admin.site.register(LandOrder, LandOrderAdmin)

# -------------------------------------------- Commercial часть -------------------------------------------- 
class CommercialAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	list_filter = ['city', 'district']
	search_fields = ['address', 'description']
	class Meta:
		model = Commercial

class CommercialOrderAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'content_object', 'suggested_price', 'order_date']
	class Meta:
		model = Commercial

admin.site.register(Commercial, CommercialAdmin)
admin.site.register(CommercialOrder, CommercialOrderAdmin)

# -------------------------------------------- Industry часть -------------------------------------------- 
class IndustryAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	list_filter = ['city', 'district']
	search_fields = ['address', 'description']
	class Meta:
		model = Industry

class IndustryOrderAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'content_object', 'suggested_price', 'order_date']
	class Meta:
		model = Industry

admin.site.register(Industry, IndustryAdmin)
admin.site.register(IndustryOrder, IndustryOrderAdmin)

# -------------------------------------------- Auto часть -------------------------------------------- 
class AutoAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	list_filter = ['brand', 'model']
	class Meta:
		model = Auto

class AutoOrderAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'content_object', 'suggested_price', 'order_date']
	class Meta:
		model = Auto

admin.site.register(Auto, AutoAdmin)
admin.site.register(AutoOrder, AutoOrderAdmin)

# -------------------------------------------- Equipment часть -------------------------------------------- 
class EquipmentAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']
	list_filter = ['brand']
	class Meta:
		model = Equipment

class EquipmentOrderAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'content_object', 'suggested_price', 'order_date']
	class Meta:
		model = Equipment

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(EquipmentOrder, EquipmentOrderAdmin)