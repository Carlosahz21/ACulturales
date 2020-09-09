# -*- coding: utf-8 -*-
import django_filters
from .models import *

# class AgrupacionFilter(django_filters.FilterSet):
# 	class Meta:
# 		model = Agrupacion
# 		fields = ["nombre_agrupacion"]
		
class ParroquiaFilter(django_filters.FilterSet):
	class Meta:
		model = Parroquia
		fields = ["nombre_parroquia"]
		
