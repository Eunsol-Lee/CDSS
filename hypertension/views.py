from django.shortcuts import render
from django.views import View
from hypertension.models import Disease, DrugType, SideEffect, Score, Disease_DrugType_Score, DrugType_DrugType_Score, SideEffect_DrugType_Score


# My own class

class ResultList():
	drugtype = "drugtype"
	description = "drug description"
	classification = "drug class"
	def __init__(self, drugtype=None, description=None, classification=None):
		self.drugtype = drugtype
		self.description = description
		self.classification = classification
	
# Create your views here.

class SimpleView(View):
	
	template_name = 'hypertension/hypertension_simple.html'
	context = {}
	drugScore = []
	drugName = []
	drugDescription = []
	drugClass = []
	drugtype_number = 5
	
	def get_default_context_data(self):
		self.context['object_list'] = ['Disease', 'DrugType', 'SideEffect']
		self.context['disease_list'] = Disease.objects.all()
		self.context['drugtype_list'] = DrugType.objects.all()
		self.context['sideeffect_list'] = SideEffect.objects.all()
		self.context['result_list'] = self.makeRecommendation()

	
	def get_selected_content_data(self, request):
		if 'disease' in request.POST:
			self.context['disease_selectedlist'] = dict(request.POST)['disease']
		if 'drugtype' in request.POST:
			self.context['drugtype_selectedlist'] = dict(request.POST)['drugtype']
		if 'sideeffect' in request.POST:
			self.context['sideeffect_selectedlist'] = dict(request.POST)['sideeffect']
	
	def get(self, request, *args, **kwargs):
		self.initialize (request)
	
		return render(request, self.template_name, self.context)
		
	def post(self, request, *args, **kwargs):
		self.initialize(request)
		
		return render(request, self.template_name, self.context) 
	
	def initialize(self, request):
		self.context = {}
		self.drugtype_number = 5
		self.drugInitialize()
		self.get_selected_content_data(request)
		self.get_default_context_data()
		
	def makeRecommendation(self):
		
		result = []
		if 'disease_selectedlist' in self.context:
			self.multiplyDiseaseDrugType(self.context['disease_selectedlist'])
		if 'drugtype_selectedlist' in self.context:
			self.multiplyDrugTypeDrugType(self.context['drugtype_selectedlist'])
		if 'sideeffect_selectedlist' in self.context:
			self.multiplySideEffectDrugType(self.context['sideeffect_selectedlist'])
			
		for i in range(self.drugtype_number):
			print (self.drugScore[i])
			if self.drugScore[i] > 1:
				self.drugClass[i] = 'class A'
			if self.drugScore[i] == 1:
				self.drugClass[i] = 'class B'
			if self.drugScore[i] < 1:
				self.drugClass[i] = 'class C'
			
			result.append(ResultList(self.drugName[i], self.drugDescription[i], self.drugClass[i]))
		
		
		return result
	
	def multiplyDiseaseDrugType(self, disease_list):
		for list in Disease_DrugType_Score.objects.all():
			for disease in disease_list:
				if str(getattr(list, 'disease')) == disease:
					
					for i in range(self.drugtype_number):
						if self.drugName[i] == getattr(list, 'drugType'):
							
							self.drugScore[i] *= getattr(list, 'score')
							self.drugDescription[i] += getattr(list, 'description') + "<br>"
	
	def multiplyDrugTypeDrugType(self, drugtype_list):
		for list in DrugType_DrugType_Score.objects.all():
			for drugtype in drugtype_list:
				if str(getattr(list, 'drugTypeB')) == drugtype:
					
					for i in range(self.drugtype_number):
						if self.drugName[i] == getattr(list, 'drugTypeA'):
							
							self.drugScore[i] *= getattr(list, 'score')
							self.drugDescription[i] += getattr(list, 'description') + "<br>"

	def multiplySideEffectDrugType(self, sideeffect_list):
		for list in sideeffect_list:
			for i in range(self.drugtype_number):
				print (list, self.drugName[i])
				print (type(list), type(self.drugName[i]))
				if str(self.drugName[i]) == list:	
					self.drugScore[i] *= 0.1
					self.drugDescription[i] += list + "에 부작용이 있음" + "<br>"
	
	def drugInitialize(self):
		self.drugScore = [1 for _ in range(self.drugtype_number)]
		self.drugName = ["" for _ in range(self.drugtype_number)]
		self.drugDescription = ["" for _ in range(self.drugtype_number)]
		self.drugClass = ["" for _ in range(self.drugtype_number)]
		
		for i in range(self.drugtype_number):
			self.drugName[i] = DrugType.objects.all()[i]
		