from django.contrib import admin

from BookStore.models import Book, Journal

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    ordering = ['name', ]


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    ordering = ['name', ]
