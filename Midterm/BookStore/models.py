from django.db import models

class BookJournalBase(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Journal(BookJournalBase):
    type = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'

