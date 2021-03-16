# ЯндексПрактикум: тема - ООП
## Проект для проведения лайва и закрепления теории
### Задача:

Необходимо создать систему регистрации экскурсионных поездок на разных видах транспорта, с возможностью узнать сколько тот или иной транспорт сможет проехать на выданном количестве топлива.
Сейчас фирма располагает экскурсионными автомобилями и легкими самолетами.
Принято, что:
- средних расход автомобилей 12л /100км
- средний расход самолетов 200кг топлива на час полета

Предполагается - программа будет создана при помощи ООП
Поскольку парк транспортных средств может расширятся, создадим базовый класс Transport (https://tatyderb.gitbooks.io/python-express-course/content/chapter_oop_advanced/oop_super.html)
```
class Transport:
    pass
```	
Каждое транспортное средство будет иметь два необходимых нам свойства - отписанное ему топливо и список экскурсий им совершенных.
Эти свойства мы будет определять в конструкторе класса __init__
(https://younglinux.info/oopython/init.php)
```
class Transport:
    def __init__(self, fuel):
        self.fuel= fuel
        self.trips = []
```
Эта запись нам говорит, что при создании экземпляра транспортного средства нам необходимо указать отписанное ему количество топлива fuel, которое присвоим свойству self.fuel.
Примечание:
для экземпляра класса название передаваемого параметра def __init__(self, fuel) и название поля self.fuel могу не совпадать
```
def __init__(self, toplivo):
        self.f= toplivo
```
и это допустимо - названия берутся для удобства, чтобы без комментариев можно было понять, какой передаваемый параметр записывается в какое поле(свойство) экземпляра класса
______________
Имя для аргумента, представляющего текущий объект класса.
self — это стандартное имя первого аргумента для методов объекта.
Ничто не мешает изменить это имя и использовать любое другое, однако пренебрежение этим устоявшимся соглашением может ввести в заблуждение читателей вашего кода.
https://pythonz.net/references/named/self/
________________
Далее для работы регистрации экскурсионных поездок нам необходим метод добавления их в список поездок add_trip
```
class Transport:
    def __init__(self, fuel):
        self.fuel= fuel
        self.trips = []
    def add_trip(self, trip):
        self.trips.append(trip)
```
Метод add_trip должен получить на вход сведения о поездке (это будет экземпляр класса Trip, который мы создадим ниже) и добавить их в наш пустой инициализированный в конструкторе список self.trips. Добавление в конец списка осуществляется методом .append(добавляемая_сущность) https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
_________________
Создадим метод расчета общей пройденной дистанции транспортным средством
```
class Transport:
    def __init__(self, fuel):
        self.fuel= fuel
        self.trips = []
    def add_trip(self, trip):
        self.trips.append(trip)
    def sum_trips_distance(self):
        return sum( trip.distance for trip in self.trips )
```
Метод sum_trips_distance(self) возвращает нам сумму всех пройденных дистанций из списка экскурсий конкретного транспортного средства
Для этого мы сформировали список уже не объектов Trip, а значений поля distance каждого объекта Trip, которые были в списке регистрации экскурсионных поездок self.trips для конкретного транспортного средства.
Запись trip.distance for trip in self.trips -это генератор списков в python (https://younglinux.info/python/feature/generators)
На выходе из генератора мы будем иметь список типа [213, 55, 345]
И его передадим функции sum, которая выполнит сложение всех элементов полученного списка (https://pythonz.net/references/named/sum/)

Еще определим метод calculate_reachable_distance, который будем переопределять в дочерних классах. Он будет нужен для определения дистанции, которую сможет пройти транспортное средство на оставшемся коилчестве топлива. 
Но сделам, так что привызове у родительского класса метод возвразал ошибку
```
def calculate_reachable_distance (self):
		raise NotImplementedError
```
___________
Для нашей задачи такого базового класса будет достаточно.
Перейдем к созданию обозначенного выше класса Trip
Объекты этого класса будут иметь два свойства - пройденную дистанцию и комментарий о цели поездки.
```
class Trip:
    def __init__(self, dist, comment = 'Не регламентировано') :
        self.distance = dist
        self.comment = comment 
```
Запись comment = 'Не регламентировано'  означает, что если мы не указываем при создании экземпляра класса значение для comment, то по умолчанию будет вписано  'Не регламентировано'.
____________

Перейдем к созданию дочерних классов транспортных средств (автомобилей и самолетов)
```
class Car (Transport):
	FUEL_CONSUMPTION_CAR = 0.12

	def calculate_reachable_distance (self):
		distance_covered = self.sum_trips_distance()
		result = (self.fuel - (distance_covered * self.FUEL_CONSUMPTION_CAR)) // self.FUEL_CONSUMPTION_CAR
		return f"Топлива осталось на {result} км."
```
и
```
class Airplane (Transport):
	FUEL_CONSUMPTION_AIRPLANE = 200

	def calculate_reachable_distance (self):
		distance_covered = self.sum_trips_distance()
		result = (self.fuel - (distance_covered * self.FUEL_CONSUMPTION_AIRPLANE)) // self.FUEL_CONSUMPTION_AIRPLANE
		return f"Топлива осталось на {result} (часы)"
```
В каждом из созданных нами классов переопределим метод возвращающий количество километром, которое еще может проехать авто на остатке топлива, и время полета, на которое хватит топливо самолету.
Переменные FUEL_CONSUMPTION_CAR и FUEL_CONSUMPTION_AIRPLANE - константы обозначающие коэффициенты для расчета.
______
Константы - переменные, значения которых никогда не меняются. Их записывают заглавными буквами. (https://pythonz.net/references/named/constants/)
______
Запись class Airplane(Transport) свидетельствует о том что мы наследуемся от базового класса Transport , а значит, все свойства и методы базового класса мы можем использовать и в дочерних.
Если не добавлять и не переопределять свойства в конструкторе дочерних классов, то конструктор в дочерних классах писать не нужно.
Далее в методах calculate_reachable_distance мы используем вызов self.sum_trips_distance() и свойство self.fuel, которые мы определяли только в родительском классе - это тоже свидетельство того, что все эти свойства и методы унаследованы.
___________________________
Полный код получившийся программы выглядит следующим образом
```
class Trip:
	def __init__(self, dist, comment= "Не регламентировано" ):
			self.distance = dist
			self.comment = comment

class Transport:
	def __init__ (self, fuel):
		self.fuel = fuel
		self.trips = []

	def add_trip (self, trip):
		self.trips.append(trip)

	def sum_trips_distance (self):
		return sum(trip.distance for trip in self.trips)

	def calculate_reachable_distance (self):
		raise NotImplementedError

class Car(Transport):
	FUEL_CONSUMPTION_CAR = 0.12

	def calculate_reachable_distance (self):
		distance_covered = self.sum_trips_distance()
		result = (self.fuel - (distance_covered * self.FUEL_CONSUMPTION_CAR)) // self.FUEL_CONSUMPTION_CAR
		return f"Топлива осталось на {result} км."

class Airplane(Transport):
	FUEL_CONSUMPTION_AIRPLANE = 200

	def calculate_reachable_distance (self):
		distance_covered = self.sum_trips_distance()
		result = (self.fuel - (distance_covered * self.FUEL_CONSUMPTION_AIRPLANE)) // self.FUEL_CONSUMPTION_AIRPLANE
		return f"Топлива осталось на {result} (часы)"
```
Для проверки программы:
создадим экземпляр одного из классов с заданием выданного топлива
добавим запись о экскурсии
выведем сколько км авто может еще проехать после нее
```
jeep = Car(80)
jeep.add_trip(Trip(dist=144, comment='туристический маршрут'))
print(jeep.calculate_reachable_distance())
```