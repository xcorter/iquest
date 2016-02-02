# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_description(apps, schema_editor):
    Quest = apps.get_model("main", "Quest")

    quests = Quest.objects.all()
    for quest in quests:
        if quest.id == 1:
            quest.description = "Ваш друг решил принять участие в безобидном медицинском исследовании, чтобы немного подзаработать, после чего бесследно пропал. Звонки по больницам и клиникам не принесли результата, и вы решили отправиться на настоящие поиски. Добравшись до неприметной больницы, на окраине города, вы встретили санитара, который рассказал вам, что ваш друг находится в закрытом крыле больницы и его держат для проведения ужасного эксперимента. У вас есть всего один час, чтобы спасти своего друга и скрыться, чтобы самим не стать жертвами таинственного доктора."
        elif quest.id == 2:
            quest.description = "Неизвестный вирус превратил жителей города в зомби. Спасательная операция завершится через час, после чего авиация сровняет это место с лицом земли. Вы оказываетесь в группе выживших, которые следуют в зону эвакуации. Ваш путь к спасению отрезан полчищами живых мертвецов от которых пришлось укрыться в ближайшем доме. Сумеете ли вы выбраться из этой западни?"
        elif quest.id == 3:
            quest.description = "Лживый донос превратилcя для вас в обвинение в государственной измене. Оказавшись в следственном изоляторе, вы узнаете, что вам уже вынесен смертельный приговор, исполнение которого назначено ровно через час. Охранник дежуривший за дверью вашей камеры срочно уехал по звонку начальства. Теперь у вас есть выбор, попытаться бежать или стать очередными жертвами режима."
        elif quest.id == 4:
            quest.description = "Как всегда, вам досталось расследование, крайне запутанного дела, о загадочных случаях, которые происходят на съемочных площадках всей страны. Нити расследования, приводят вас прямиком к съемочному павильону, проникнуть внутрь которого удается без особых проблем. Однако, все это не спроста. Вы угодили прямиком в ловушку и теперь все зависит только от вас."
            quest.is_active = True
        elif quest.id == 5:
            quest.description = "Гениальный (по другим версиям немного сумасшедший) профессор Файнгерц, в плотную подошел к созданию прибора, способного значительно повысить уровень интеллекта, любого человека. Это открытие, могло бы дать огромный толчок в развитии науки, но буквально на днях, профессор бесследно пропал. Теперь вы, как его ближайшие ученики, должны выяснить, что с ним произошло и связанно ли это с его изобретением?"
        quest.save()



class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20160201_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='description',
            field=models.TextField(verbose_name='Описание квеста', default=''),
            preserve_default=True,
        ),
        migrations.RunPython(add_description)
    ]