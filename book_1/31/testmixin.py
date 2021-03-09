"""
Обобщённый инструмент тестирования подмешиваемых классов вывода списков:
он похож на средство транзитивной перезагрузки модулей из главы 25 первого
тома, но ему передаётся объект класса (не функции), а в testByNames
добавлена загрузка модуля и классса по строковым именам в соответствии с
паттерном проектирования "Фабрика"
"""

import importlib


def tester(listerclass, sept=False):
    class Super:
        def __init__(self):  # Метод __init__ суперкласса
            self.data1 = 'spam'  # Создать атрибуты экземпляра

        def ham(self):
            pass

    class Sub(Super, listerclass):  # Подмешивание ham и __str__
        def __init__(self):  # Классы, выводящие списки атрибутов, имеют доступ к self
            Super.__init__(self)
            self.data2 = 'eggs'  # Дополнительные атрибуты экземпляра
            self.data3 = 42

        def spam(self):  # Определить здесь ещё один метод
            pass

    instance = Sub()  # Возратить экземпляр с помощью __str__ класса, выводящего список
    print(instance)  # Выполняется подмешенный метод __str__ (или через str())
    if sept: print('-' * 80)


def testByNames(modname, classname, sept=False):
    modobject = importlib.import_module(modname)  # Импортировать по строковым именам
    listerclass = getattr(modobject, classname)  # Извлечь аттрибуты по строковым именам
    tester(listerclass, sept)


if __name__ == '__main__':
    testByNames('listinstance', 'ListInstance', True)
    testByNames('listinherited', 'ListInherited', True)
    testByNames('listintree', 'ListTree', True)

