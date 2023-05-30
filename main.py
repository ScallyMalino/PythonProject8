import time
def calculate_time(func):
    def wrapper(a, b):
        start_time = time.time()
        result = func(a, b)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Вычисление заняло: {:.6f} секунд".format(execution_time))
        print("Размеры сторон: {}, {}".format(a, b))
        print("Результат: {}".format(result))
        return result
    return wrapper

@calculate_time
def calculate_hypotenuse(a, b):
    return (a**2 + b**2)**0.5

a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

calculate_hypotenuse(a, b)
