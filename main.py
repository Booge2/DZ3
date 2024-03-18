class Person:

    def __init__(self, full_name: str, date_of_birth: str, phone_number: str, city: str, country: str,
                 home_address: str):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def __str__(self):
        return f"""
        **ПІБ:** {self.full_name}
        **Дата народження:** {self.date_of_birth}
        **Телефон:** {self.phone_number}
        **Місто:** {self.city}
        **Країна:** {self.country}
        **Домашня адреса:** {self.home_address}
        """

    def change_phone_number(self, new_phone_number: str):
        self.phone_number = new_phone_number

    def move_to_new_address(self, new_city: str, new_country: str, new_home_address: str):
        self.city = new_city
        self.country = new_country
        self.home_address = new_home_address


person1 = Person(
    full_name="Іванов Іван Іванович",
    date_of_birth="1980-01-01",
    phone_number="+380991234567",
    city="Київ",
    country="Україна",
    home_address="вул. Шевченка, 1",
)

print(person1)

person1.change_phone_number("+380978901234")
person1.move_to_new_address("Львів", "Україна", "вул. Франка, 10")

print(person1)
# Завдання 2
class City:

    def __init__(self, name: str, region: str, country: str, population: int, postal_code: str, phone_code: str):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def __str__(self):
        return f"""
        **Місто:** {self.name}
        **Регіон:** {self.region}
        **Країна:** {self.country}
        **Населення:** {self.population}
        **Поштовий індекс:** {self.postal_code}
        **Телефонний код:** {self.phone_code}
        """

    def change_population(self, new_population: int):
        self.population = new_population

    def update_postal_code(self, new_postal_code: str):
        self.postal_code = new_postal_code


city1 = City(
    name="Київ",
    region="Київська область",
    country="Україна",
    population=2962150,
    postal_code="01001",
    phone_code="044",
)

print(city1)

city1.change_population(2963000)
city1.update_postal_code("01002")

print(city1)
# Завдання 3
from typing import List


class Country:

    def __init__(self, name: str, continent: str, population: int, phone_code: str, capital: str, cities: List[str]):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def __str__(self):
        return f"""
        **Країна:** {self.name}
        **Континент:** {self.continent}
        **Населення:** {self.population}
        **Телефонний код:** {self.phone_code}
        **Столиця:** {self.capital}
        **Міста:** {", ".join(self.cities)}
        """

    def add_city(self, new_city: str):
        self.cities.append(new_city)

    def change_capital(self, new_capital: str):
        self.capital = new_capital


country1 = Country(
    name="Україна",
    continent="Європа",
    population=44134693,
    phone_code="+380",
    capital="Львів",
    cities=["Львів", "Одеса", "Дніпро"],
)

print(country1)

country1.add_city("Харків")
country1.change_capital("Київ")

print(country1)
