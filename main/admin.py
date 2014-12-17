from django.contrib import admin
from main.models import GiftCardOrder, QuestOrder, Time, Quest


class QuestOrderAdmin(admin.ModelAdmin):
    list_display = ('quest', 'time', 'date')
    date_hierarchy = 'date'

admin.site.register(GiftCardOrder)
admin.site.register(QuestOrder, QuestOrderAdmin)
admin.site.register(Time)
admin.site.register(Quest)
