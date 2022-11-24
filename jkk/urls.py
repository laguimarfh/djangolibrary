from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.jkks8View.as_view(), name='jkkhome'),
    # path('jkkperiod/<int:pk>', views.periodjkkView.as_view(), name='periodjkk'),
    # path('jkkcheck/', views.checkjkkView.as_view(), name='checkjkk'),
    # path('jkkperiod/', views.periodjkkView.as_view(), name='jkkperiod'),
    # path('stopwatch/', views.stopwatchView.as_view(), name='stopwatch'),
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)