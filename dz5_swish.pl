% Rules
% sum_elements([X],X).
sum_elements([],0).
sum_elements([H|T],Sum):-
    sum_elements(T,Sum1),
    Sum is Sum1 + H.
    
% Rules_v2
sum_lists(List, Sum) :- 
    foldl(plus, List, 0, Sum).

% Rules_v3
:- use_module(library(lists)).

sum_lists_v3(List, Sum) :- sum_list(List, Sum).