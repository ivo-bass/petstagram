from django.contrib import admin

from petstagram.pets.models import Pet, Like


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'age', 'likes_count', )
    list_filter = ('type', )
    sortable_by = ('id', 'name', 'age', )

    def likes_count(self, obj):
        return obj.like_set.count()


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
