# Парадигмы Программирования

### DZ1
### Задача №1
- Дан список целых чисел numbers.
- Необходимо написать в императивном стиле процедуру для сортировки числа в списке в порядке убывания.
- Можно использовать любой алгоритм сортировки.
### Задача №2
- Написать точно такую же процедуру, но в декларативном стиле
- Решение: [PythonDZ1](https://github.com/555-F-a-r-id-555/Programming-Paradigms/blob/master/dz1.py "PythonDZ")

### DZ2
### Таблица умножения
- Домашнее задание
- ● Условие
- На вход подается число n.
- ● Задача
- Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n. 
- Обоснуйте выбор парадигм.
- Решение: [PythonDZ2](https://github.com/555-F-a-r-id-555/Programming-Paradigms/blob/master/dz2.py "PythonDZ")
### DZ3
### Крестики нолики
- ● Задача
- Написать игру в “Крестики-нолики”. Можете использовать
- любые парадигмы, которые посчитаете наиболее
- подходящими. Можете реализовать доску как угодно - как
- одномерный массив или двумерный массив (массив массивов).
- Можете использовать как правила, так и хардкод, на своё
- усмотрение. Главное, чтобы в игру можно было поиграть через
- терминал с вашего компьютера
- Решение: [PythonDZ3](https://github.com/555-F-a-r-id-555/Programming-Paradigms/blob/master/dz3 "PythonDZ")

### DZ4
### Корреляция Пирсона 

- ● Контекст
- Корреляция - статистическая мера, используемая для оценки связи между двумя случайными величинами.
- ● Ваша задача
-Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).
- Можете использовать любую парадигму, но рекомендую использовать функциональную, 
- т.к. в этом примере она значительно упростит вам жизнь.
- Решение: [PythonDZ4](https://github.com/555-F-a-r-id-555/Programming-Paradigms/blob/master/dz4.py "PythonDZ")

 
### DZ5
### Сумма элементов списка на языке Prolog
- ● Ваша задача
- Написать программу на языке Prolog для вычисления суммы 
- элементов списка. На вход подаётся целочисленный массив. 
- На выходе - сумма элементов массива.

-  Решение:
``` prolog
% Rules
sum_elements([],0).
sum_elements([H|T],Sum):-
    sum_elements(T,Sum1),
    Sum is Sum1 + H.

% Query
% ?- sum_elements([1,2,3,4,5], Sum).
% Sum = 15.
```
- v2,v3
```prolog
% Rules_v2
sum_lists(List, Sum) :-
    foldl(plus, List, 0, Sum).

% Query
% ?- sum_lists([1,2,3,4,5], Sum).
% Sum = 15.


% Rules_v3
:- use_module(library(lists)).
sum_lists_v3(List, Sum) :- sum_list(List, Sum).

% Query_v3:
% ?- sum_lists_v3([1,2,3,4,5], Sum).
% Sum = 15.

```
- Решение: [PythonDZ5](https://github.com/555-F-a-r-id-555/Programming-Paradigms/blob/master/dz5.pl "PythonDZ")

### DZ6
### Бинарный поиск
```text
Ваша задача:
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.
```
``` python

    def binary_search(num_list, n, count=0):
        if not num_list:
            return -1
        
        middlle = len(num_list) // 2
        left_half = num_list[:middlle]
        right_half = num_list[middlle + 1:]
        
        if num_list[middlle] == n:
            return count + middlle
        elif num_list[middlle] > n:
            return binary_search(left_half, n, count)
        else:
            return binary_search(right_half, n, count + middlle + 1)
```

- Решение: [PythonDZ6](https://github.com/555-F-a-r-id-555/Programming-Paradigms/blob/master/dz6.py "PythonDZ")
