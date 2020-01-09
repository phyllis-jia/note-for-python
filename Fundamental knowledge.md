# Fundamental knowledge

## basic
- Element in array: first is 0(positive), first is -1(negative)
- *:all, ?:one
- **T**rue==1 (r: **TRUE**)
- Empty:{}  []     
- Axis=1----row  axis=0---column
- Index(): position
- Count(): number
- Range(start,stop,step) （don't include stop!!）
-  ~：reverse

# event
- Xxx[row,column]
- -：Del()
- +：+ []
- Replace：X[]=new
- To check whether include: .. In …
- Keys():Return a new view of the dictionary’s keys

## comparison of tuple, list, array, dict, set, series, DataFrame
- Tuple:() (if you want a function to return multiple values, you can just return a tuple)(ordered)(can not change)
- List:[] (ordered)

 delete:1.pop() --if none,delete the end,or delete index one; 2.remove('')

 add: 1.append():add in the end one by one; 2.extend():add a lot of data in the end; 3.insert(index, value)

(list can be comprehensive, [[output expression] for iterator  variable in iterable if condition of iterator//  [[output expression] if-else for iterator variable in iterable] e.g. [(num1,num2) for num1 in range(1,3) for num2 in range(2,4)]

- Array: np.array([same type data]) (fixed size) (index) (append, extend) (different dimension array)
- Dict: {} (key-value)(unordered) (dict() )
- Set:()  like an unordered List (mainly use for extisting reasearch)(case sensitilve,add(),remove(),can use for)(unordered)
- Series:one-dimensional array&dict, index(can change，like key)，multiple types
- DataFrame: conbined many arrays，use usually，how to deal with like cleaning data

## basic function
1. Function: def xx():

The program reads the return () statement, and the subsequent statements will not be executed.

The print () statement is different. Subsequent statements will still execute.

2. Lambda: lambda(x,y):…
- *single value* Map(function, seq) (print result, it's directly whole result，list(result) is separate result )
- *single value* Filter(lambda x: …., z)
- *multi-value* Reduce(functions, seq) (import from functools)
3. loop
- while
- if
- Elif
- else

(if not xxx ----xxx: zero, empty, False)

4. Apply
apply(func,*args,**kwargs)

Dataframe: xxx.apply(func)

**if there are many variables for function, it may lead errors. So use xxx.apply(function)**

5. Enumerate(seq, start=n): (for all result using list() )

6. Zip(): an iterator of tuples (*: unzip)

7. Matrix: matrix = [[col for col in range(n)] for row in range(n)] 

8. mean：xxx.mean()

when exchange columns, df[a,b]=df[b,a] will lead error, to solve it using loc/iloc

for boolean, when we want detailed value, use loc/iloc

e.g Cars.loc['eu']

9. loc & iloc

- loc doesn't like python, it's like MATLAB's bilateral closed interval
- iloc like python

slice : [::n] = [start, stop, step]

10. import time

time.time(): returns the time as a floating point number expressed in seconds since the epoch, in UTC.

11.xx.join(xxx) --- e.g ''join(xxx) --- 'xxx'

12. matrix

- [[a,b,c...],[x,y,z...]....]

- [[x*y for x in xxx] for y in yy]
