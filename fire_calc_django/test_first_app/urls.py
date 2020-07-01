from django.urls import path, include

from test_first_app import views


urlpatterns = [
    # path('test_first_app/', include('test_first_app.urls')),
    path('', views.index, name='index'),
    path('help/', views.help_page, name='help')
    # path('admin/', admin.site.urls),
]
