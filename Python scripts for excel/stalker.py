from random import randint


class Stalker():
    def __init__(self):
        self.move_speed = 5
        self.health = 100
        self.stamina = 100
        self.name = self.add_name()
        self.rank, self.rank_point = self.add_rank()
        self.carry_weight = 40
        self.clan = self.add_clan()
        self.armor = self.add_armor()
        self.first_weapon, self.second_weapon = self.add_weapon()
        self.weight = 3

    def add_clan(self):
        clans = ['Долг', 'Нейтрал', 'Свобода', 'Наёмники', 'Монолит', 'Бандиты']
        return clans[randint(0, len(clans)-1)]

    def add_name(self):
        names = ['Ваня', 'Лёха', 'Серёга', 'Миха', 'Игорь', 'Влад', 'Олег', 'Паша', 'Дима', 'Вован', 'Денис', 'Илюха',
                 'Герман', 'Марк', 'Валера', 'Никита', 'Вован', 'Миша', 'Андрей', 'Стас', 'Егор', 'Жека', 'Тимур',
                 'Матвей', 'Артем', 'Митяй', 'Альберт', 'Тарас', 'Руслан', 'Алекс', 'Антон', 'Борис', 'Степан',]
        last_names = ['Кащей', 'Ведьмак', 'Сивый', 'Боров', 'Тихий', 'Серый', 'Черный', 'Череп', 'Турбо', 'Шнырь','Крот',
                      'Омон', 'Кирпич', 'Червонец', 'Битум', 'Ловкий', 'Барыга', 'Стальной', 'Камень', 'Старый','Демон',
                      'Язычник', 'Ястреб', 'Картон', 'Бегемот', 'Ловчий', 'Медведь', 'Леший', 'Толстый', 'Наука','Дуремар',
                      'Мумия', 'Зомби', 'Танк', 'Крокодил', 'Свирепый', 'Кулак', 'Труба', 'Цемент', 'Дикий', 'Устав',
                      'Гонщик', 'Повар', 'Князь', 'Шутник', 'Охотник', 'Кривой', 'Удача', 'Пулемет', 'Опасный', 'Удав',
                      'Артист', 'Грек', 'Рус', 'Упырь', 'Дед', 'Кабан', 'Жулик', 'Якорь', 'Арбалет', 'Музыкант', 'Орк',
                      'Гном', 'Жидкий', 'Зоркий', 'Клещ', 'Завод', 'Гром', 'Амбал', 'Инженер', 'Индус', 'Север','Вампир',
                      'Груз', 'Гомер', 'Генератор', 'Костыль', 'Козырь', 'Пряник', 'Пожар', 'Вулкан', 'Жмур', 'Хлопец',
                      'Бурят', 'Китаец', 'Космонавт', 'Тополь', 'Аллигатор', 'Эконом', 'Игрок', 'Южный', 'Комар',
                      'Горец', 'Камыш', 'Крыша', 'Медь', 'Громкий', 'Борзый', 'Могильщик', 'Партизан', 'Жуков', 'Зуб',
                      'Лопата', 'Кувалда', 'Тяжелый', 'Тупик', 'Немец', 'Бритва', 'Кран', 'Глаз', 'Троян', 'Шуруп',
                      'Гроб', 'Лом', 'Движок', 'Рыбак', 'Зеленый', 'Синий', 'Сова', 'Черпак', 'Ухо', 'Дух', 'Кочерга',
                      'Полено', 'Фен', 'Кальмар', 'Паштет', 'Доллар', 'Банан', 'Парашют', 'Кобра', 'Ванга', 'Юрист',
                      'Пиджак', 'Огурец', 'Агент', 'Кепка', 'Лысый', 'Бармалей', 'Кутузов', 'Камаз', 'Крутой', 'Лентяй',
                      'Электрик', 'Удав', 'Бобер', 'Витязь', 'Шомпол', 'Затвор', 'Дырчик', 'Заноза', 'Нервный', 'Клык',
                      'Лотос', 'Меткий', 'Кот', 'Змей', 'Мангуст', 'Добрый', 'Лекарь', 'Арбуз', 'Холера', 'Ячмень',
                      'Поляк', 'Хитрый', 'Белорус', 'Бочка', 'Сверло', 'Перфоратор', 'Ветер', 'Прораб', 'Вахтер',
                      'Яркий', 'Молот', 'Шланг', 'Гвоздь', 'Страж', 'Монгол', 'Ловец', 'Пузырь', 'Белый', 'Аргон',
                      'Дон', 'Дуб', 'Математик', 'Варяг', 'Дрозд', 'Зяблик', 'Оркестр', 'Алфавит', 'Боец', 'Воин',
                      'Сутулый', 'Чувак', 'Штурмовик', 'Стажёр', 'Счастливый', 'Фортуна', 'Хмурый', 'Богатырь', 'Амбал',
                      'Бессмертный', 'Олигарх', 'Депутат', 'Шишак', 'Пузо', 'Лунатик', 'Шмель', 'Аскет', 'Веселый',
                      'Маэстро', 'Модный', 'Умник', 'Шустрый', 'Локомотив', 'Орех', 'Длинный', 'Ветеран', 'Волк',
                      'Туземец', 'Аномалия', 'Паук', 'Монах', 'Борода', 'Турист', 'Зануда', 'Гриб', 'Клинок', 'Хищник',]
        uses_names = []
        name = None
        # print(f'names all: {len(names) * len(last_names)}')
        while not name and name not in uses_names:
            name = names[randint(0, len(names)-1)] + ' ' + last_names[randint(0, len(last_names)-1)]
        uses_names.append(name)
        return name

    def add_rank(self):
        ranks = ['Новичек', 'Опытный', 'Ветеран', 'Мастер']
        rank = ranks[randint(0, 3)]
        if rank == 'Новичек':
            rank_point = randint(0, 150)
        elif rank == 'Опытный':
            rank_point = randint(150, 400)
        elif rank == 'Ветеран':
            rank_point = randint(400, 800)
        else:
            rank_point = randint(800, 999)
        return rank, rank_point

    def add_armor(self):
        armors_light = ['Крутка новичка', 'Куртка бандита', 'Кожанный плащ']
        armors_middle = ['Комбенизон заря', 'Ветер свободы', 'Комбинезон Долга', 'Комбинезон наемника']
        armors_high = ['Комбинезон СЕВА', 'Страж свободы', 'Бронекостюм Булат', 'ССП-99М']
        armors_havy= ['Экзоскелет', 'СКАТ 9М']
        if self.rank == 'Новичек':
            armor = armors_light[randint(0, len(armors_light) - 1)]
        elif self.rank == 'Опытный':
            armor = armors_middle[randint(0, len(armors_middle) - 1)]
        elif self.rank == 'Ветеран':
            armor = armors_high[randint(0, len(armors_high) - 1)]
        else:
            armor = armors_havy[randint(0, len(armors_havy) - 1)]
        return armor

    def add_weapon(self):
        first_weapon = 'FN 2000'
        second_weapon = 'Colt M1911'
        light_weapon = ['Обрез', 'Мр-5', 'АК-74У', 'МР-153', 'СКС']
        middle_weapon = ['АК-74М', 'АК-74', 'АК-103', 'AR-15', 'МР-155', 'Витязь 19-01', 'CZ-805 BREN', 'АС ВАЛ',
                         'AUG A3', 'AR-15 custom', 'SCAR L', 'Mossberg 800 custom', 'ВСС']
        high_weapon = ['АС ВАЛ', 'ВСС', 'АК-12', 'AR-15 custom', 'SCAR H', 'G36', 'FN 2000', 'SCAR L']
        heavy_weapon = ['ПКМ', 'USAS-12', 'РПЛ', 'СВД-М', 'AR-15 DMR', 'СВ-98']
        pistols = ['ПМ', 'ЯП Грач', 'Beretta 92 FS', 'Glock 18', 'USP 45', 'P226', 'CZ-75']
        if self.rank == 'Новичек':
            first_weapon = light_weapon[randint(0, len(light_weapon)-1)]
            second_weapon = pistols[randint(0, len(pistols)-4)]
        elif self.rank == 'Опытный':
            first_weapon = middle_weapon[randint(0, len(middle_weapon)-1)]
            second_weapon = pistols[randint(0, len(pistols)-1)]
        elif self.rank == 'Ветеран':
            first_weapon = middle_weapon[randint(0, len(middle_weapon)-1)]
            second_weapon = pistols[randint(1, len(pistols)-1)]
        else:
            first_weapon = high_weapon[randint(0, len(high_weapon)-1)]
            second_weapon = pistols[randint(3, len(pistols)-1)]
        if self.rank_point > 930:
            first_weapon = heavy_weapon[randint(0, len(heavy_weapon)-1)]
            second_weapon = pistols[randint(len(pistols)-3, len(pistols)-1)]
        return (first_weapon, second_weapon)

    def run(self, time):
        if self.weight == self.carry_weight:
            print('Вы перегруженны и не можете бежать!')
        elif self.weight == self.carry_weight - 10:
            while self.stamina != 10 or time != 0:
                self.move_speed = 12
                self.stamina -= 3
                time -= 1
            self.move_speed = 5
        else:
            while self.stamina != 10:
                self.move_speed = 12
                self.stamina -= 1
            self.move_speed = 5

    def move(self, time):
        if self.weight == self.carry_weight - 10:
            while self.stamina != 10 or time != 0:
                time -= 1
        else:
            while self.stamina != 10:
                self.stamina += 1
                time -= 1

    def description(self):
        return (f'Имя: {self.name} \n'
              f'Группировка {self.clan}\n'
              f'Ранг: {self.rank}\n'
              f'Опыт: {self.rank_point}\n'  
              f'Оружие: {self.first_weapon}  пистолет: {self.second_weapon} \n'
              f'Комбинезон: {self.armor} \n'
              f'Состояние здоровья: {self.health} %\n\n\n')


# with open('stalkers.txt', 'w') as file_object:
#     for i in range(0, 6030):
#         npc = Stalker()
#         file_object.write(f'№ {i}\n')
#         file_object.write(str(npc.description()))
#
#
# npc = Stalker()
# print('doc ', Stalker.__doc__)
# print('dict', len(Stalker.__dict__))
# print(npc.description())

