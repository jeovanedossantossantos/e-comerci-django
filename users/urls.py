
from django.urls import path

from .views import CreateUserView, UserViewsPrivate, UserViewsPublic
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.urlpatterns import format_suffix_patterns
# https://github.com/rg3915/gallery/blob/master/gallery
urlpatterns = [
     path('user/', csrf_exempt(CreateUserView.as_view())),
     path('user/teste/list/',UserViewsPublic.ListUsersView.as_view()),
     path('user/private/<id>/',UserViewsPrivate.as_view()),
     path('user/public/<id>/',UserViewsPublic.as_view()),
     path('token/', TokenObtainPairView.as_view() ),
     path('token/refresh/', TokenRefreshView.as_view()),
    
     # path('token/refresh/', TokenRefreshView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)