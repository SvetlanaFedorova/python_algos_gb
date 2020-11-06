"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""
def search_user(dict_user):
    search_login = input('Введите логин: ')
    if search_login.title() != dict_user['login']:
        return print('Некорректный логин')
    search_parol = input('Введите пароль: ')
    if search_parol != dict_user['parol']:
        return print('Некорректный пароль')
    if dict_user['activ'] == 'no':
        search_activ = input('Для продолжения, прошу активировать учетную запись: '
                             ' Нажмите: Да - yes, Нет - no ')
        if search_activ.lower() == 'no':
            return print('Отказано в доступе без активации учетной записи. Попробуйте еще раз!')
        if search_activ.lower() == 'yes':
            dict_user['active'] = 'yes'
            return dict_user, print('Добро пожаловать!')
        else:
            return print('Отказано в доступе без активации учетной записи. Попробуйте еще раз!')
    return dict_user, print('Добро пожаловать!')

dict_user = {'login': 'Ivanov', 'parol': '123', 'activ': 'no'}
res = search_user(dict_user)

'''2 Вариант 
Данный алгоритм содержит цикл в цикле, что увеличивает время выполнения. Причем, время будет тем 
стремительнее увеличиваться, чем больше будет величины счетчиков на прерываение циклов (i, j).
Поэтому я считаю, что алгоритм имеет квадратичную ложность - O(n^2). 
'''
def search_user(dict_user):
    i = 1
    while True:
        search_login = input('Введите логин: ')
        search_parol = input('Введите пароль: ')
        if search_login.title() != dict_user['login'] or search_parol != dict_user['parol']:
            print('Некорректный логин или пароль')
            i += 1
            if i > 3:
                break
            continue
        j = 1
        while True:
            if dict_user['activ'] == 'no':
                search_activ = input('Для продолжения, прошу активировать учетную запись: '
                             ' Нажмите: Да - yes, Нет - no ')
                if search_activ.lower() == 'yes':
                    dict_user['active'] = 'yes'
                    print("Добро пожаловать!")
                    return dict_user
                print('Отказано в доступе без активации учетной записи. Попробуйте еще раз!')
                j += 1
                if j > 3:
                    print('Вы превысили лимит попыток. Попробуйте с начала!')
                    break
                continue
            print("Добро пожаловать!")
            return dict_user
    return print('Вы превысили лимит попыток. Попробуйте с начала!')

dict_user = {'login': 'Ivanov', 'parol': '123', 'activ': 'no'}
res = search_user(dict_user)

''' 3 вариант
Алгоритм имеет перебор элементов for in, а в остальном время выполнения постоянное (константа).
Общее время выполнения алгоритмя будет прямопропорционально зависеть от входных данных 
по количеству попыток. Поэтому алгоритм имеет линейную сложность - O(n). 
'''
def search_user(dict_user):
    for el in range(1, 4):
        print(f"У Вас 3 попытки ввести правильные данные. Попытка № {el} ")
        search_login = input('Введите логин: ')
        if search_login.title() != dict_user['login']:
            print('Некорректный логин. Попробуйте заново')
            continue
        search_parol = input('Введите пароль: ')
        if search_parol != dict_user['parol']:
            print('Некорректный пароль. Попробуйте заново')
            continue
        if dict_user['activ'] == 'no':
            search_activ = input('Для продолжения, прошу активировать учетную запись: '
                                 ' Нажмите: Да - yes, Нет - no ')
            if search_activ.lower() == 'yes':
                dict_user['active'] = 'yes'
                return dict_user, print("Добро пожаловать!")
            print('Отказано в доступе без активации учетной записи. Попробуйте еще раз!')
            continue
        dict_user['active'] = 'yes'
        return dict_user, print("Добро пожаловать!")
    return dict_user, print("Вы превысили лимит попыток. Попробуйте заново!")

dict_user = {'login': 'Ivanov', 'parol': '123', 'activ': 'no'}
res = search_user(dict_user)
