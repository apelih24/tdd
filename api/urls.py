from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.authtoken import views
from .views import CreateView, DetailsView

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('create/', CreateView.as_view(), name='create'),
    path('books/<int:pk>/', DetailsView.as_view(), name='details'),
    # path('get-token/', views.obtain_auth_token)

]

urlpatterns = format_suffix_patterns(urlpatterns)
