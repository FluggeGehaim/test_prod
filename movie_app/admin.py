from django.contrib import admin, messages
from .models import Movie, Director
from django.db.models import QuerySet

# Register your models here.
admin.site.register(Director)


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('от 80', 'Великолепно'),

        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == 'от 80':
            return queryset.filter(rating__gte=80)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    # exclude = ['slug']
    readonly_fields = ['currency']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'director', 'year', 'currency', 'rating', 'budget', 'slug', 'rating_status']
    list_editable = ['director', 'year', 'rating', 'currency', 'budget', 'slug']
    ordering = ['name', 'rating']
    list_per_page = 5
    actions = ['currency_usd', 'currency_eur']
    search_fields = ['name', 'rating__startswith']
    list_filter = ['name', RatingFilter]

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Это плохо'
        if movie.rating < 70:
            return 'На один разон'
        if movie.rating <= 85:
            return 'Очень даже'
        return 'Топ'

    @admin.action(description='Установить USD')
    def currency_usd(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить EUR')
    def currency_eur(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.EUR)
        self.message_user(request,
                          f'Было обновлено {count_update} записей', messages.INFO)
