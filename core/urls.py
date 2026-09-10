from django.urls import path
from . import views

#app_name = 'core'

urlpatterns = {
    path('', views.index, name='urlindex'),
    path('analise01/', views.line_chart_view, name="urlanalise01"),
    path('analise02/', views.bar_chart_view, name="urlanalise02"),
    path('analise03/', views.line_chart_view, name="urlanalise03"),
    path('analise04/', views.line_chart_view, name="urlanalise04"),
    path('analise05/', views.line_chart_view, name="urlanalise05"),
}