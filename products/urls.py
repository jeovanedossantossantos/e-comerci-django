from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from products.views import CreateCategoryView
urlpatterns = [
    path('register/', CreateCategoryView.as_view()),
    path('list/', CreateCategoryView.as_view()),
    path('<id>/', CreateCategoryView.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)