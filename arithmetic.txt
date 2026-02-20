% Arithmetic operations
add(X, Y, Z) :-
    Z is X + Y.

subtract(X, Y, Z) :-
    Z is X - Y.

multiply(X, Y, Z) :-
    Z is X * Y.

divide(X, Y, Z) :-
    Y \= 0,
Z is X / Y.
remainder(X, Y, Z) :- Z is X mod Y. 
% Comparison example 
greater(X, Y) :- X > Y.

Queries and Output
Query 1:add(10, 5, R).
Output: R = 15.
Query 2: subtract(10, 3, R).
Output: R = 7.
Query 3: multiply(4, 6, R).
Output: R = 24.
Query 4: divide(20, 5, R).
Output: R = 4.
