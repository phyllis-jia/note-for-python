# Iterator & iterable & generator

for x in y
- y: iterable, 可用for x in y: print x **-all**(实际的可迭代对象：actual list)
- x: iterator，可以next() **-一个一个**（虚拟迭代器：不一次性生成，需要时调用）
1. iterable--iterator: iter()
*for iter(), iter(iterable)--iterator ; iter(iterator)--self*
2. iterator--iterable: list()
*list取值可用index, iterator 只能next()用['name']*
range()是iterator, 取chunk 
惰性求值(Lazy evaluation): 迭代器不要求你事先准备好整个迭代过程中所有的元素。迭代器仅仅在迭代至某个元素时才计算该元素，而在这之前或之后，元素可以不存在或者被销毁
- generator(更简洁的迭代器):  (don't store in computer, big data will not break down) (yield; .items, range)
1. （[output expression] for iterator  variable in iterable if condition of iterator)  or  ([output expression] if-else for iterator variable in iterable)   e.g. ((num1,num2) for num1 in range(1,3) for num2 in range(2,4))
2. yield
**List &generator 的区别**
1. Generator:  (  )       (虚拟)
2. List:  [  ]   (real)
*E.g:     generator:       lengths = (len(person) for person in lannister) 
              list:                    lengths = [len(person) for person in lannister]*
generator和普通函数对比代码见后面

