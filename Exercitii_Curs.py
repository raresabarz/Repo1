'''
Iterators

Implementati un iterator numit ReverseIterator, care parcurge o colectie in sens opus. Exemplu de folosire:

note = [3, 7, 5, 8, 10]
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
s.a.m.d

'''
import functools
from contextlib import contextmanager
from datetime import datetime
from random import randint
from time import perf_counter, sleep


class ReverseIterator:
    def __init__(self, colection):
        self.colection = colection
        self.start = len(colection) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration

        current_index = self.start
        self.start -= 1
        return self.colection[current_index]


note = [3, 7, 5, 8, 10]
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
rev_it = ReverseIterator(note)
for elem in rev_it:
    print(elem)

'''
Generators

Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv)
Ultima apelare va da un singur număr de “noroc” format din 7 cifre
'''
print(60 * '~')


def loterie_gen():
    for i in range(6):
        yield randint(1, 49)
    yield randint(1000000, 9999999)


for i in loterie_gen():
    print(i)


def loterie_gen_unice():
    generate = set()
    for i in range(6):
        nr = randint(1, 49)
        while nr in generate:  # cat timp nr generat a mai fost generat inca o data
            nr = randint(1, 49)
        generate.add(nr)  # adauga nr noi in setul de numere generate pana acum
        yield nr
    yield randint(1000000, 9999999)


for i in loterie_gen_unice():
    print(i)

for i in loterie_gen():
    print(i)

'''
Decorators

Implementați următorii decoratori:
timeit – decorator care măsoară timpul de execuție al unei funcții 
logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții
'''
print(60 * '~')


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f'A durat {perf_counter() - start} secunde')
        return result

    return wrapper


@timeit
def say_hello():
    sleep(3)
    print('Functie executata')


say_hello()


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Rezultat: {result}')
        print(f'Argumente pozitionale: {args}')
        print(f'Argumente cu nume: {kwargs}')

    return wrapper


@logger
def name(first, last):
    return f'{first} - {last}'


name('Adrian', last='Andrei')

'''
Decorators extra

Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nasterii 
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat, folosind un decorator `@require_login` 
– o metoda logout, fara params, care delogheaza userul.


Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.
'''
print(60 * '~')


def require_logged_in(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_logged_in:
            return func(self, *args, **kwargs)

    return wrapper


class User:
    def __init__(self, nume, email, parola, data_nasterii):
        self.nume = nume
        self.email = email
        self.parola = parola
        self.data_nasterii = data_nasterii
        self.__logat = False

    def login(self, email, parola):
        if email == self.email and parola == self.parola:
            self.__logat = True

    @require_logged_in
    def get_info(self):
        return f'Nume: {self.nume}, Email: {self.email}, Data Nasterii: {self.data_nasterii}, Parola: {"*" * len(self.parola)}'

    def logout(self):
        self.__logat = False

    @property
    def is_logged_in(self):
        return self.__logat


u = User('Adrian Andrei', 'adrianandrei@gmail.com', 'parola123', '01.01.90')
print(u.get_info())
u.login('adrianandrei@gmail.com', 'parola123')
print(u.get_info())
u.logout()
print(u.get_info())

'''
6. Sa se scrie un decorator care primeste ca parametru doua ore, 
reprezentand datele limita intre care sa se execute functiile decorate.
'''

print(60 * '~')


def only_execute_between(start, end):
    def decorator_execute_between(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if start <= datetime.now().hour <= end:
                return func(*args, **kwargs)

        return wrapper

    return decorator_execute_between


@only_execute_between(19, 23)
def hello():
    print('Hello World!')


hello()

'''
2. Sa se scrie un context manager care masoara durata de executie a codului din interiorul sau
'''
print(60 * '~')


class Timer:
    def __enter__(self):
        self.start = perf_counter()
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'A durat {perf_counter() - self.start} secunde ')


with Timer():
    sleep(3)
    print('M-am trezit!')


@contextmanager
def timer():
    start = perf_counter()
    yield
    print(f'A durat {perf_counter() - start}')


print(20 * '~')
with timer():
    sleep(3)
    print('M-am trezit!')

'''
3. Sa se scrie un generator care primeste ca parametru un string 
si genereaza cate un caracter in ordine inversa a aparitiei in string
'''
print(60 * '~')


def rev_str_gen(string):
    length = len(string)
    for i in range(length - 1, -1, -1):
        yield string[i]


for elem in rev_str_gen('abcd'):
    print(elem)



