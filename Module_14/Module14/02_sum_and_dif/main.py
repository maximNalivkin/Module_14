# TODO здесь писать код
def num_sum(var):
    total = 0
    for i in var:
        total += int(i)
    print('\nСумма чисел: {}'.format(total))
    return total - num_count(number)


def num_count(var):
    count = 0
    for _ in var:
        count += 1
    print('Количество цифр в числе: {}'.format(count))
    return count


number = input('Введите число: ')
print('Разность суммы и количества цифр: {}'.format(num_sum(number)))
