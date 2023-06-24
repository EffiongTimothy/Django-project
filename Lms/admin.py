from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BasedUserAdmin
# Register your models here.
from Lms.models import Author, Book, BookInstance, User


@admin.register(User)
class UserAdmin(BasedUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['email']
    list_per_page = 10


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'language', 'genre']
    # list_filter = ['date_added']
    list_per_page = 20


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = []

# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
# admin.site.register(BookInstance)
