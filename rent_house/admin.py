from django.contrib import admin, messages
from rent_house.models import Appartments, Category


@admin.register(Appartments)
class AppartmentsAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','photo','payment','number_of_rooms','size_of_apartment','floor','furniture','technique','cat','is_published']
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title','time_create','photo','payment','is_published','cat']
    list_display_links = ['title']
    ordering = ['time_create']
    list_per_page =5
    list_editable = ['is_published']
    actions = ['set_published','set_draft']
    save_on_top = True

    @admin.action(description='Опубликовать выбранные посты')
    def set_published(self,request,queryset):
        count = queryset.update(is_published=True)
        self.message_user(request,f'Изменено {count} записей')

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Category)
class AppartmentsAdmin(admin.ModelAdmin):
    fields = ['title','slug',]
    prepopulated_fields = {'slug':('title',)}