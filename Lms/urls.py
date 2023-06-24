from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)
urlpatterns = router.urls
#
# urlpatterns = [
#     # path('all_author/', views.all_author, name='home'),
#     # path('authors/<int:pk>', views.AuthorDatailView.as_view(), name='author-detail'),
#     path('list_authors/', views.AuthorView.as_view()),
#     path('send_mail/', views.send_mail_function)
# ]
# # path('list_books/', views.all_books),
# path('book_detail/<int:pk>/', views.book_detail),

#
#
#
#
#     # path('list_authors/', views.AuthorView.as_view()),
#     # path('welcome/', views.welcome),
# ]
