"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""


def simple(i):  # O(n^2)
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


def eratosthenes(n):  # O(n log n)
    x = n * 10
    check = [False] * x
    res = []
    for i in range(2, x):  # O(n)
        if check[i]:
            continue
        for j in range(i * 2, x, i):  # O(log n)
            check[j] = True
        res.append(i)
    return res[n - 1]


"""
number = 100

simple(10) --> 0.0015545999999999963
eratosthenes(10) --> 0.0015072000000000002

simple(100) --> 0.24502240000000003
eratosthenes(100) --> 0.029566800000000004

simple(1000) --> 33.4858652
eratosthenes(1000) --> 0.1741883

Судя по данным замера примерно одинаковый результат показывают обе функции
при небольшом принимаемом значекнии, однако при увеличении диапазона поиска
метод через перебор делителей силино замедляеться по времени исполнения
Это объясняется более высокой сложностью алгоритма по сравнению с методом Эротосфена.
В некоторых источниках я также встречал что метод через перебор делителей это O(2^n)
судя по замерам очень на то похоже, но в ситуации с вышепреведённым алгоритмом это скорее O(n^2).
Судя по данным Википедии сложность алгоритма "Решето Эротосфена" состовляет O(n log(log n))
но в моей реализации я не пришёл к такому результату или может я ошибаюсь что сложность
в моём примере будет O(n log n). Наставьте меня на путь истинный :)
"""
