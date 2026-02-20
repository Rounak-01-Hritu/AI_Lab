% Tower of Hanoi program

hanoi(1, Source, Destination, _) :-
    write('Move disk from '),
    write(Source),
    write(' to '),
    write(Destination), nl.

hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, Source, Auxiliary, Destination),
    write('Move disk from '),
    write(Source),
    write(' to '),
    write(Destination), nl,
    hanoi(N1, Auxiliary, Destination, Source).
Queries and Output
Query
hanoi(3, left, right, middle).
Output
Move disk from left to right
Move disk from left to middle
Move disk from right to middle
Move disk from left to right
Move disk from middle to left
Move disk from middle to right
Move disk from left to right