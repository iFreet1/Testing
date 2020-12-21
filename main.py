# a = list(map(int, input().split()))

# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# if auth:
#     username = input("Введите ваш username:")
#
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#     return wrapper
#
#
# def has_access(func):
#     def wrapper():
#         if username in USERS:
#             print('Авторизован')
#             func()
#         else:
#             print('Не авторизован')
#
#     return wrapper
#
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
#
# from_db()

# print(any(a))

# gen_a = [int(input()) % 2 == 0 for i in range(5)]

# print(gen_a)
# print(not any(a))

# if all([type(a) == int, 100 <= a <= 999, a % 2 == 0 and a % 3 == 0]):
#     print("Подходит")


# L = ['THIS', 'IS', 'LOWER', 'STRING']
#
# print(list(map(str.lower, L)))
#
# for i in map(str.lower, L):
#     print(i)

# some_list = [1, -3, -4, 6]
#
# print([i**2 for i in some_list if i > 0])

# d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
#
# # Чтобы отсортировать его по ключам нужно сделать так
# print(dict(sorted(d.items())))
# print(dict(sorted(d.items(), key = lambda x: x[1])))  # сортировка по значению словаря


# # (вес, рост)
# data = [
#    (82, 191),
#    (68, 174),
#    (90, 189),
#    (73, 179),
#    (76, 184)
# ]
#
# d = {82 : 191, 83 : 191, 84 : 191, 85 : 191}
#
#
# print(min(sorted(data, key=lambda x: x[0]/(x[1]**2))))


a = ["asd", "bbd", "ddfa", "mcsa"]

print(list(map(len, a)))

a = ["это", "маленький", "текст", "обидно"]

print(list(map(str.upper, a)))