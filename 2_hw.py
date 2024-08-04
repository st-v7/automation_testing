def task_1():
    var_int: int = 7
    var_float: float = 3.1415
    var_str: str = "завершить гештальт"
    var_list: list = [1, 2, 3, 4, 5]
    var_bool: bool = True

print(type(var_int))
print(type(var_float))
print(type(var_str))
print(type(var_list))
print(type(var_bool))

# вызов функции
task_1()


def task_2():
    a: list[int] = [1, 2, 3, 5, 8, 13, 21] Числа Фибоначчи
print(a[:3])

# вызов функции
task_2()


def task_3(number: int):
    return number ** 2

# вызов функции и распечатка результата
print(task_3(5))  # пример вызова функции с числом 5
