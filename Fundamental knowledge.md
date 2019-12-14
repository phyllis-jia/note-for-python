# Fundamental knowledge

## basic
- Element in array: first is 0（正）, first is -1  (负)
- *:全部可能, ?:一个可能
- **T**rue==1 (r: **TRUE**)
- Empty:{}  []     
- Axis=1----row  axis=0---column
- Index():位置
- Count():数量
- Range(start,stop,step) （不包括stop）
-  ~：反转

# 项
- Xxx[row,column]
- -：Del()
- +：+ []
- Replace：X[]=new
- To check whether include: .. In …
- Keys():Return a new view of the dictionary’s keys

## comparison of tuple, list, dict, set, series, DataFrame
- Tuple(元组):() (如果你希望一个函数返回多个返回值，其实只要返回一个tuple就可以了)（有序）（不可变）
- List:[] (delete:1.pop() --if none,delete the end,or delete index one; 2.remove('') add: 1.append():add in the end one by one; 2.extend():add a lot of data in the end; 3.insert(index, value))（有序）(list 可comprehensive, [[output expression] for iterator  variable in iterable if condition of iterator//  [[output expression] if-else for iterator variable in iterable] e.g. [(num1,num2) for num1 in range(1,3) for num2 in range(2,4)]
- Dict: {} (key-value, 建值方式加项）（无序）(dict() )
- Set:()  类似于一个无序List (主要用来找是否存在)(大小写是敏感的,add(),remove(),可用for)（无序）
- Series:一维数组&dict，可改，有index(可改，更像key)，多种类型
- DataFrame: 多个数组组成，常用，处理可看cleaning data

##basic function
1. Function: def xx():
程序读到return()语句,其后的语句不会再被执行,
而print（）语句不同，其后的语句依然会被执行
2. Lambda: lambda(x,y):…
- *single value* Map(function, seq) (如果直接print result，就是直接结果，list（result）就是分项的结果 )
- *single value* Filter(lambda x: …., z)
- *multi-value* Reduce(functions, seq) (import from functools)
3. loop
- while
- if
- Elif
- else
4. Apply
apply(func,*args,**kwargs)
Dataframe: xxx.apply(func)
**当定义的function参数导致的结果众多，会产生错误用参数.apply(function)**
5. Enumerate(seq, start=n):遍历 (想要all用list() )
6. Zip(): an iterator of tuples (*: unzip)
7. Matrix: matrix = [[col for col in range(n)] for row in range(n)] 
8. mean：xxx.mean()
当交换列 普通python选择（df[a,b]=df[b,a]）报错，利用loc/iloc切片
当得到boolean，想要具体value，可用loc/iloc切片
Cars.loc['eu']
9. loc & iloc
- loc索引的开闭区间机制和Python传统的不同，而是与MATLAB类似的双侧闭区间
- iloc索引的开闭区间机制与python相同

