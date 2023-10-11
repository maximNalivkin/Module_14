# TODO здесь писать код


def calculate(var):
    for i in range(2, var + 1):
        if var % i == 0:
            return i


print('Наименьший делитель, отличный от единицы:', calculate(int(input('Введите число: '))))
