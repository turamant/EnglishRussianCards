#!/usr/bin/env python3
'''
Написать программу карточки для заучивания слов Англ - Русский
1)Пары слов - словарь dict
2)Генератор случайных слов(карточек
3)Модуль ввод новых пар слов(карточек
4)Модуль -=Режим заучивания=-
5)Режим Тест
  5.1 Учет правильно отвеченных и неправильно отвеченных
  5.2 Процент успешного усвоения материала

1 Этап
-------
Делаем на словаре
Сливаем все в файл

2 Этап
-------
Прикручиваем БД sqlite



'''


#  НАЧАЛО ПРОГРАММЫ СОБСТВЕННО

import shelve
import random
from tkinter import *

def print_hi(name):
    print(f'Hi, {name}')
    print("Программа словарный запас!")

def slovar_create():
    ''' Добавляет новые пары слов в Базу данных(словарь)
    :return: void '''
    while True:
        print("Введите пары слов:")
        print("Для выхода из режима создания нажмите q или Q")
        engl = str(input("English: "))
        if engl == 'q' or engl == 'Q':
            break
        if engl in file:
            print("Английское слово уже есть,\n"
                  " введите новый перевод на русском")
        rusk = str(input("Russian: "))
        file[engl] = rusk


def show_all(list_keys, f):
    '''  Демонстрация всех пар слов из словаря БД
     :return: void '''
    print("Словарь отсортирован: ")
    print(40 * "=")
    count_words = 0
    for i in list_keys:
        print('\t',i, '\t\t          \t\t', f[i])
        count_words += 1
    print(40 * "=")
    print(f"Итого   :    {count_words} пар слов")
    print(25 * "=")


def slovar_show_all(f):
    ''' универсальная функция -готовит отсортированный список ключей
    :return: void'''
    list_keys = list(f.keys())
    list_keys.sort()
    show_all(list_keys, f)


def delete_words():
    ''' Удаляет ключи по запросу из словаря БД
    :return: void '''
    while True:
        slovar_show_all(file)
        print("Для удаления введите слово на английском")
        print("Для выхода из режима создания нажмите q или Q")
        engl = str(input("English: "))
        if engl == 'q' or engl == 'Q':
            break
        if engl in file:
            print(f"({engl} : {file[engl]}) удалено!")
            del file[engl]
        else:
            print("Такого слова нет!")


def random_card_words(f):
    '''
    :param f: file shelve
    :return: void
    '''
    count_right = 0
    count_error = 0
    list_error =[]
    slovar_error = {}
    while True:
        print("Для выхода из режима создания нажмите букву 'й' или Й'")
        print(50 *"=")
        engl = random.choice(list(f.keys()))
        print(f"Введите правильный перевод этого слова\n\t -= {engl.capitalize()} =-")
        print(50 * "=")
        russ = str(input("Русский: "))
        if russ == 'й' or russ == 'Й':
            print(f"Всего проверено слов: {count_right+count_error} Правильно: {count_right} Неправильно {count_error}")
            print(f"Вы отвечали неправильно {count_error} раза: {list_error}")
            print("А правильно так: ")
            for k,v in slovar_error.items():
                print('\t',k,'\t  :  \t', v)
            break
        if russ == f[engl]:
            print(f"!!! -= Правильно!=- : ({engl} :: {f[engl]})\n")
            count_right += 1
        else:
            err_file(engl)
            list_error.append(russ)
            slovar_error[engl] = f[engl]
            print("Error")
            print(f"Правильно: ({engl} :: {f[engl]})\n")
            count_error += 1

def err_file(engl):
    '''
    записывает ошибочные слова в словарь/файл ошибок
    :param engl:
    :return:
    '''
    err[engl] = file[engl]
    print("Error")

def one_func_random(f):
    '''
    универсальная процедура - случайные пары слов(карточек)
    для всего словаря и для словаря ошибок
    :param f:
    :return:
    '''
    while True:
        print("Для выхода из режима создания нажмите букву 'й' или Й'")
        engl = random.choice(list(f.keys()))
        print(f"Введите правильный перевод этого слова\n\t -= {engl.capitalize()} =-")
        russ = str(input("Русский: "))
        if russ == 'й' or russ == 'Й':
            break
        if russ == f[engl]:
            print(f"!!! -= Правильно!=- : ({engl} :: {f[engl]})\n")
        else:
            err_file(engl)

def slovar_game_over():
    print("Good bye!")
    print("Copyright (c) askvart")


def user_case(case):
    '''
    функция switch case
    :param case: выбор ветки программы
    :return:
    '''
    if case == 1:
        slovar_create()
    if case == 2:
        slovar_show_all(file)
    if case == 3:
        delete_words()
    if case == 4:
        #OneFuncRandom(file)
        random_card_words(file)
    if case == 5:
        slovar_show_all(err)
    if case == 6:
        #OneFuncRandom(err)
        random_card_words(err)
    if case == 8:
        slovar_game_over()
        return 8

def print_case():
    print("1 - Добавить словарные пары  "
          "2 - показать весь словарь 3-удалить слова из словаря "
          " 4 - случайная карточка" "5 - Показать словарь ошибок"
          "6 - Работа со словарем ошибок"   "8 - выход из программы")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('WordsCards')
    namefile = "slovar.dat"
    namefile2 = "error.dat"
    try:
        with shelve.open(namefile) as file:
            with shelve.open(namefile2) as err:
                while True:
                    print_case()
                    case = int(input("Ведите: "))
                    if user_case(case) == 8:
                        break
    except FileNotFoundError:
        print("Нет такого файла!")
    else:
        print("Все прошло Ok")
