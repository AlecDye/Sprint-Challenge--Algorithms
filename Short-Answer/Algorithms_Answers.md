#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

```python
a)  a = 0
    while (a < n * n * n): # O(1)
      a = a + n * n
```

a) O(1)

```python

sum = 0
for i in range(n):
  j = 1
  while j < n: # O(n)
    # if this was / it would be log n?
    # not sure what \* is
    j \* = 2
    sum += 1

```

b) O(n)

```python

def bunnyEars(bunnies):
  if bunnies == 0:
    return 0

  return 2 + bunnyEars(bunnies-1) # O(1)?

```

c) O(1)

## Exercise II

```
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
```

```
n = building height (number of floors)
f = boundary
f >= broken egg
f < safe egg

find ideal max boundary

Start at n/2 (middle) to determine if egg breaks
ex: n = 10 f = 5 (n/2)

If egg survives -> increment the floor up 1 and rerun

else (egg breaks) -> decrement the floor down 1

Checking 2 conditions with 1 loop

Return condition (egg break confirmed) -> reassign f to last run floor and subtract 1 (len(arr)-1 to get true position)

runtime is O(log n) since we run 2 conditions per loop?

```
