class Tomato:
    # Статическое свойство, содержащее стадии созревания помидора
    states = {0: 'Отсутствие завязи', 1: 'Цветение', 2: 'Зеленый', 3: 'Спелый'}

    def __init__(self, index):
        # _index - уникальный индекс томата
        # _state - текущая стадия созревания, изначально первая стадия из states
        self._index = index
        self._state = 0  # Начальное состояние: 0 (Отсутствие завязи)

    def grow(self):
        # Переводит томат на следующую стадию созревания, если она не максимальная
        if self._state < max(self.states):
            self._state += 1

    def is_ripe(self):
        # Проверяет, достиг ли томат последней стадии созревания (3 - Спелый)
        return self._state == max(self.states)


class TomatoBush:
    def __init__(self, count):
        # tomatoes - список объектов Tomato, количество задается параметром count
        self.tomatoes = [Tomato(index) for index in range(count)]

    def grow_all(self):
        # Переводит все томаты в кусте на следующую стадию созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Проверяет, все ли томаты в кусте достигли стадии "Спелый"
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Очищает куст, убирая все томаты (сбор урожая)
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        # name - имя садовника (публичное свойство)
        # _plant - растение, за которым ухаживает садовник (объект TomatoBush)
        self.name = name
        self._plant = plant

    def work(self):
        # Ухаживает за растением, переводя все его томаты на следующую стадию созревания
        print(f"{self.name} ухаживает за растением...")
        self._plant.grow_all()

    def harvest(self):
        # Если все томаты созрели, собирает урожай; если нет, предупреждает об этом
        if self._plant.all_are_ripe():
            print("Все томаты созрели. Собираем урожай!")
            self._plant.give_away_all()
        else:
            print("Томаты еще не созрели. Необходимо больше ухода.")

    @staticmethod
    def knowledge_base():
        # Выводит справку по садоводству
        print("Справка по садоводству:\n"
              "1. Ухаживайте за растением, чтобы томаты созревали.\n"
              "2. Сбор урожая возможен только после полного созревания томатов.\n"
              "3. Следите за стадиями созревания томатов и ухаживайте за ними регулярно.")

# Тесты

# Вызов справки по садоводству
Gardener.knowledge_base()

# Создание объекта TomatoBush с 3 томатами
bush = TomatoBush(3)

# Создание садовника для ухода за кустом
gardener = Gardener("Анна", bush)

# Уход за кустом с помидорами
gardener.work()  # Первая стадия ухода
gardener.harvest()  # Попытка собрать урожай (еще не созрел)

# Повторный уход
gardener.work()  # Вторая стадия ухода
gardener.harvest()  # Попытка собрать урожай (еще не созрел)

# Третий этап ухода, после которого томаты должны созреть
gardener.work()
gardener.harvest()  # Теперь томаты должны быть собраны, так как они созрели
