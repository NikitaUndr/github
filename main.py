import math
'''
class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        distance = math.sqrt((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2 + (z - self.center[2]) ** 2)
        return distance <= self.radius


sphere1 = Sphere(2)

volume = sphere1.get_volume()
square = sphere1.get_square()
print("Объем:", volume)
print("Площадь:", square)

radius = sphere1.get_radius()
center = sphere1.get_center()
print("Радиус:", radius)
print("Центр:", center)

sphere1.set_radius(3)
sphere1.set_center(1, 2, 3)
print("Новый радиус:", sphere1.get_radius())
print("Новый центр:", sphere1.get_center())

point_inside = sphere1.is_point_inside(1, 2, 3)
print("Точка внутри сферы:", point_inside)
'''
'''
class SuperStr(str):
    def is_repeatance(self, s):
        if not s or len(self) % len(s) != 0:
            return False
        return self == s * (len(self) // len(s))

    def is_palindrom(self):
        return self.lower() == self[::-1].lower()


s = SuperStr('abcabcabcabc')
print(s.is_repeatance('abc'))
print(s.is_repeatance('abcabc'))
print(s.is_repeatance('ab'))

p = SuperStr('abccba')
print(p.is_palindrom())
'''

'''
2. ПчёлоСлон
class Elephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        return self.bee >= self.elephant

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elephant -= value
            self.bee += value
        elif meal == "grass":
            self.elephant += value
            self.bee -= value

        if self.elephant > 100:
            self.elephant = 100
        elif self.elephant < 0:
            self.elephant = 0

        if self.bee> 100:
            self.bee = 100
        elif self.bee < 0:
            self.bee = 0


beelephant = Elephant(70, 30)

print(beelephant.fly())
print(beelephant.trumpet())

beelephant.eat("nectar", 20)
print(beelephant.bee)
print(beelephant.elephant)
'''

'''
1. Класс «Товар» ()
class Product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    def get_info(self):
        return f"Товар: {self.__name}\nМагазин: {self.__store}\nЦена: {self.__price} руб."

    def get_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_price(self):
        return self.__price


class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def get_product_by_index(self, index):
        if index >= 0 and index < len(self.__products):
            return self.__products[index].get_info()
        else:
            return "Товар с указанным индексом не найден."

    def get_product_by_name(self, name):
        for product in self.__products:
            if product.get_name() == name:
                return product.get_info()
        return "Товар с указанным именем не найден."

    def sort_by_name(self):
        self.__products.sort(key=lambda x: x.get_name())

    def sort_by_store(self):
        self.__products.sort(key=lambda x: x.get_store())

    def sort_by_price(self):
        self.__products.sort(key=lambda x: x.get_price())

    def __add__(self, other):
        if isinstance(other, Warehouse):
            new_warehouse = Warehouse()
            new_warehouse.__products = self.__products + other.__products
            return new_warehouse
        else:
            return self

    def __str__(self):
        result = ""
        for product in self.__products:
            result += product.get_info() + "\n\n"
        return result.strip()


product1 = Product("Монитор", "Магазин1", 10000)
product2 = Product("Клавиатура", "Магазин2", 1500)
product3 = Product("Мышь", "Магазин1", 500)

warehouse = Warehouse()
warehouse.add_product(product1)
warehouse.add_product(product2)
warehouse.add_product(product3)

print(warehouse.get_product_by_index(1))

print(warehouse.get_product_by_name("Мышь"))

warehouse.sort_by_name()
print(warehouse)

warehouse2 = Warehouse()
warehouse2.add_product(Product("Наушники", "Магазин2", 2000))
warehouse3 = warehouse + warehouse2
print(warehouse3)
'''