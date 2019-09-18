from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('register', views.register, name='register')
	#url(r'^ix_tutor/', include('ix_tutor.urls')),
    #url(r'^admin/', admin.site.urls),
]
