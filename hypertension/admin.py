from django.contrib import admin
from .models import Disease
from .models import DrugType
from .models import SideEffect
from .models import Score
from .models import Disease_DrugType_Score
from .models import DrugType_DrugType_Score
from .models import SideEffect_DrugType_Score


# Register your models here.
admin.site.register(Disease)
admin.site.register(DrugType)
admin.site.register(SideEffect)
admin.site.register(Score)
admin.site.register(Disease_DrugType_Score)
admin.site.register(DrugType_DrugType_Score)
admin.site.register(SideEffect_DrugType_Score)