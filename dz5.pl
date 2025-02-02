% Rules_v1
% sum_elements([X],X).
sum_elements([],0).
sum_elements([H|T],Sum):-
    sum_elements(T,Sum1),
    Sum is Sum1 + H.

% Query
% ?- sum_elements([1,2,3,4,5], Sum).
% Sum = 15.



% Rules_v2
sum_lists(List, Sum) :-
    foldl(plus, List, 0, Sum).

% `plus/3` — встроенный арифметический оператор: plus(A, B, C) => C = A + B.
% Query
% ?- sum_lists([1,2,3,4,5], Sum).
% Sum = 15.

% Rules_v3
:- use_module(library(lists)).

sum_lists_v3(List, Sum) :- sum_list(List, Sum).

% Query_v3:
% ?- sum_lists_v3([1,2,3,4,5], Sum).
% Sum = 15.