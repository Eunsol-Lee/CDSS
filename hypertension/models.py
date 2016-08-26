from django.db import models


# Create your models here.

class Disease(models.Model):
	name = models.CharField(max_length=200, unique=True)
	
	def __str__(self):
		return self.name
		

class DrugType(models.Model):
	name = models.CharField(max_length=20, unique=True)
	
	def __str__(self):
		return self.name
		
class SideEffect(models.Model):
	name = models.CharField(max_length=20, unique=True)
	
	def __str__(self):
		return self.name

class Score(models.Model):
	score = models.FloatField()
	title = models.CharField(max_length=50, unique=True)
	description = models.TextField()
	
	def __str__(self):
		return self.title
	
class Disease_DrugType_Score(Score):
	disease = models.ForeignKey(Disease)
	drugType = models.ForeignKey(DrugType)
		
class DrugType_DrugType_Score(Score):
	drugTypeA = models.ForeignKey(DrugType, related_name='drugTypeA')
	drugTypeB = models.ForeignKey(DrugType, related_name='drugTypeB')
	
class SideEffect_DrugType_Score(Score):
	sideEffect = models.ForeignKey(SideEffect)
	drugType = models.ForeignKey(DrugType)
	