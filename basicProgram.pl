% Facts
parent(john, mary).
parent(john, tom).
parent(mary, lisa).
parent(tom, alex).

male(john).
male(tom).
male(alex).

female(mary).
female(lisa).

% Rules
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
Queries and Output
Query 1: father(john, mary).
Output: true.
Query 2: mother(mary, lisa).
Output: true.
Query 3: grandparent(john, lisa).
Output: true.
Query 4: father(X, alex).
Output: X = tom.