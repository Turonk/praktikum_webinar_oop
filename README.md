# ЯндексПрактикум: тема - ООП

## Проект для проведения лайва и закрепления теории

### Задача

Необходимо создать систему регистрации экскурсионных поездок на разных видах транспорта с возможностью узнать сколько тот или иной транспорт сможет проехать на выданном количестве топлива.

Сейчас фирма располагает экскурсионными автомобилями и легкими самолетами.

Принято, что:

- средний расход автомобилей 12л/100км
- средний расход самолетов 200кг топлива на час полета

Предполагается — программа будет создана при помощи ООП.

Поскольку парк транспортных средств может (и будет!) расширяться, кажется целесообразным использовать ООП.

Начнем с создания базового класса `Transport` (https://tatyderb.gitbooks.io/python-express-course/content/chapter_oop_advanced/oop_super.html).

```python
class Transport:
	pass
```

Каждое транспортное средство будет иметь два необходимых нам свойства - выданное ему топливо и список совершенных им экскурсий.

Эти свойства мы будем определять в "конструкторе" (инициализаторе) `__init__` (https://younglinux.info/oopython/init.php).

```python
class Transport:
    def __init__(self, fuel):
        self.fuel = fuel
        self.trips = []
```

Эта запись нам говорит, что при создании экземпляра транспортного средства нам необходимо указать выданное ему количество топлива `fuel`, которое присвоим свойству `self.fuel`.

Примечание: для экземпляра класса название передаваемого параметра `def __init__(self, fuel)` и название поля `self.fuel` не обязаны совпадать.

```python
def __init__(self, toplivo):
    self.f = toplivo
```

Так можно, но кому от этого проще? Названия подбираются для удобства, чтобы без комментариев можно было понять, какой передаваемый параметр записывается в какое поле (свойство) экземпляра класса.

---

<details>

<summary>Да кто такой этот ваш self ?!</summary>

Имя для первого аргумента, представляющего текущий объект класса, self — это стандартное имя первого аргумента для методов объекта.

Ничто не мешает изменить это имя и использовать любое другое, однако пренебрежение этим устоявшимся соглашением может ввести в заблуждение читателей вашего кода.

https://pythonz.net/references/named/self/

</details>

---

Далее, для регистрации экскурсионных поездок нам необходим метод добавления их в список поездок — `add_trip`.

```python
class Transport:
    def __init__(self, fuel):
        self.fuel = fuel
        self.trips = []

    def add_trip(self, trip):
        self.trips.append(trip)
```

Метод `add_trip` должен получать на вход сведения о поездке (это будет экземпляр класса `Trip`, который мы создадим ниже) и добавлять ее в наш список `self.trips`. Добавление в конец списка осуществляется методом `.append(добавляемая сущность)`.

Подробнее: https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html.

---

Создадим метод расчета общей пройденной дистанции транспортным средством.

```python
class Transport:
    def __init__(self, fuel):
        self.fuel = fuel
        self.trips = []
    
    def add_trip(self, trip):
        self.trips.append(trip)
    
    def sum_trips_distance(self):
        return sum(trip.distance for trip in self.trips)
```

Метод `sum_trips_distance(self)` возвращает нам сумму всех пройденных дистанций из списка экскурсий конкретного транспортного средства.

Для этого мы сформировали список уже не объектов `Trip`, а значений поля `distance` каждого объекта `Trip`, которые были в списке регистрации экскурсионных поездок `self.trips` для конкретного транспортного средства.

Запись `trip.distance for trip in self.trips` — это генератор списков в python (https://younglinux.info/python/feature/generators).

На выходе из генератора мы получим последовательность вида `[213, 55, 345]`. Это будет именно **последовательность**, а не список, так что работать с генератором как с обычным списком нельзя. Можно превратить результат генератора в список, например, так: `list(trip.distance for trip in self.trips)`. Но функция `sum` отлично справляется и со списками и с генераторами, поэтому просто применяем ее к генератору (https://pythonz.net/references/named/sum/).

Еще определим метод `calculate_reachable_distance`, который будем переопределять в дочерних классах. Он будет нужен для определения дистанции, которую сможет пройти транспортное средство на оставшемся количестве топлива.

Но сделам так, что при вызове у родительского класса метод будет генерировать ошибку.

```python
def calculate_reachable_distance(self):
    raise NotImplementedError()
```

Для нашей задачи такого базового класса будет достаточно.

---

Перейдем к созданию обозначенного выше класса `Trip`.

Объекты этого класса будут иметь два свойства — пройденную дистанцию и комментарий о цели поездки.

```python
class Trip:
    def __init__(self, dist, comment='Не регламентировано'):
        self.distance = dist
        self.comment = comment
```

Запись `comment = 'Не регламентировано'` означает, что если мы не указываем при создании экземпляра класса значение для `comment`, то по умолчанию будет подставлено `'Не регламентировано'`.

---

Перейдем к созданию дочерних классов транспортных средств (автомобилей и самолетов).

```python
class Car(Transport):
    FUEL_CONSUMPTION_CAR = 0.12

    def calculate_reachable_distance(self):
        distance_covered = self.sum_trips_distance()
        result = (self.fuel - (distance_covered * self.FUEL_CONSUMPTION_CAR)) // self.FUEL_CONSUMPTION_CAR
        return f'Топлива осталось на {result} км'
```

```python
class Airplane(Transport):
    FUEL_CONSUMPTION_AIRPLANE = 200

    def calculate_reachable_distance(self):
        distance_covered = self.sum_trips_distance()
        result = (self.fuel - (distance_covered * self.FUEL_CONSUMPTION_AIRPLANE)) // self.FUEL_CONSUMPTION_AIRPLANE
        return f'Топлива осталось на {result} часов'
```

В каждом из созданных нами классов переопределим метод возвращающий количество километров, которое еще может проехать авто на остатке топлива, и время полета, на которое хватит топлива самолету.

Переменные `FUEL_CONSUMPTION_CAR` и `FUEL_CONSUMPTION_AIRPLANE` — константы обозначающие коэффициенты для расчета.

---

<details>

<summary>Пара слов о константах</summary>

Константы — переменные, значения которых никогда не меняются.

Их записывают заглавными буквами (https://pythonz.net/references/named/constants/).

В python это договоренность, нежели ограничение языка, поменять можно все :) Но договоренности надо соблюдать.

</details>

---

Запись `class Airplane(Transport)` свидетельствует о том что мы наследуемся от базового класса `Transport`, а значит, все свойства и методы базового класса мы можем использовать и в дочерних классах.

Если не добавлять и не переопределять свойства в конструкторе дочерних классов, то конструктор в дочерних классах писать не нужно.

Далее в методах `calculate_reachable_distance` мы используем вызов `self.sum_trips_distance()` и свойство `self.fuel`, которые мы определяли только в родительском классе — это тоже свидетельство того, что все эти свойства и методы унаследованы.

---

<details>

<summary>Полный код получившийся программы</summary>

```python
class Trip:
    def __init__(self, dist, comment="Не регламентировано"):
        self.distance = dist
        self.comment = comment


class Transport:
    def __init__(self, fuel):
        self.fuel = fuel
        self.trips = []

    def add_trip(self, trip):
        self.trips.append(trip)

    def sum_trips_distance(self):
        return sum(trip.distance for trip in self.trips)

    def calculate_reachable_distance(self):
        raise NotImplementedError()


class Car(Transport):
    FUEL_CONSUMPTION_CAR = 0.12

    def calculate_reachable_distance(self):
        distance_covered = self.sum_trips_distance()
        result = (self.fuel - (distance_covered * self.FUEL_CONSUMPTION_CAR)) // self.FUEL_CONSUMPTION_CAR
        return f'Топлива осталось на {result} км'


class Airplane(Transport):
    FUEL_CONSUMPTION_AIRPLANE = 200

    def calculate_reachable_distance(self):
        distance_covered = self.sum_trips_distance()
        result = (self.fuel - (distance_covered * self.FUEL_CONSUMPTION_AIRPLANE)) // self.FUEL_CONSUMPTION_AIRPLANE
        return f'Топлива осталось на {result} часов'
```

</details>

---

Для проверки работоспособности программы создадим экземпляр одного из классов и зададим количество выданного топлива.

Затем добавим запись об экскурсии.

И наконец, выведем информацию об оставшихся возможностях.

<details>

<summary>Код проверки работоспособности</summary>

```python
jeep = Car(80)
jeep.add_trip(Trip(dist=144, comment='туристический маршрут'))
print(jeep.calculate_reachable_distance())
```

Должно вывестись следующее:

```
Топлива осталось на 522.0 км
```

</details>
