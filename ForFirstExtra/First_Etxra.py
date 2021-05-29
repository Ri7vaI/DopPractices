"""
Первая часть 1 практики:
Некто попытался реализовать "наивную" функцию умножения с помощью сложения.
К сожалению, в коде много ошибок. Сможете ли вы их исправить?
Добавьте к naive_mul автоматическое тестирование для проверки обоих
аргументов в диапазоне от 0 до 100. Сравнивайте с встроенным умножением,
используя конструкцию assert.
"""


def native_mul(x, y, res=0):
    for _ in range(y):
        res += x
        return x


def test_native_mul():
    for x in range(101):
        for y in range(101):
            assert native_mul(x, y) == x * y
    print("Все тесты пройдены")


test_native_mul()