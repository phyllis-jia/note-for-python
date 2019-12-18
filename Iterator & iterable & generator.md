# Iterator & iterable & generator

for x in y
- y: iterable, can use for x in y: print x **--all**(actual list)
- x: iterator，can use next() **--one by one**（virtual iterator: not make at one time. when we need it, we will take one to use）

1. iterable--iterator: iter()
*for iter(), iter(iterable)--iterator ; iter(iterator)--self*

2. iterator--iterable: list()
*list can use index, iterator use next(), which can only utilizing ['name']*

range() is iterable, use chunk 

Lazy evaluation: an evaluation strategy which delays the evaluation of an expression until its value is needed (non-strict evaluation) and which also avoids repeated evaluations (sharing)

3. generator(more concise iterator):  (don't store in computer, big data will not break down) (yield; .items, range)
- ([output expression] for iterator  variable in iterable if condition of iterator)  or  ([output expression] if-else for iterator variable in iterable)   e.g. ((num1,num2) for num1 in range(1,3) for num2 in range(2,4))
- yield

**comparison of List &generator **

1. Generator:  (  )       (virtual)

2. List:  [  ]   (real)

*E.g:     generator:       lengths = (len(person) for person in lannister) 

              list:                    lengths = [len(person) for person in lannister]*

generator & normal code is attached

