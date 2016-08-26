from django.conf.urls import url
from hypertension import views

urlpatterns = [
	url(r'^$', views.SimpleView.as_view(), name='Simple'),

]
