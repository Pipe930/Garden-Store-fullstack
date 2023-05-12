from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlsCategory = [
    path('', views.ListCategoriesView.as_view()),
    path('created', views.CreateCategoryView.as_view()),
    path('category/<int:id>', views.CategoryDetailView.as_view()),
    path('category/update/<int:id>', views.UpdateCategoryView.as_view()),
    path('category/delete/<int:id>', views.DeleteCategoryView.as_view()),
]

urlsCategory = format_suffix_patterns(urlsCategory)
