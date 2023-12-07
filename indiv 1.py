#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Ввести список одной строкой.
    A = tuple(map(int, input("Введите мощности через пробел: ").split()))
    B = tuple(map(int, input("Введите стоимости через пробел: ").split()))
    # Проверить количество элементов списка.
    if len(A) != 30 or len(B) != 30:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    # Найти искомую сумму.
    prices = [index for item, index in zip(A, B) if item < 80]
    print("Цены: ", prices)
