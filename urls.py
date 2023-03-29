from django.urls import include,path
from .views import analytics
from . import views
from .views import bar_graph
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_app.urls')),
    path('reports_dashboard/', analytics, name='reports_dashboard'),
    path('bar-graph/', bar_graph, name='bar_graph'),
    path('export-csv/', views.export_csv, name='export_csv'),
    
]