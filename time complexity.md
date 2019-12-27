# time complexity

running time: best case(lower bound on cost); average case(random input);worse case(upper bound on cose)(focus on)

running time: constant (O(1)) < logarithmic (O(lgn)) < linear (O(n)) < nlogn(O(nlogn) < quadratic(O(n^2) < exponential < cubic

big-o ------- O(f(n)) : running time max limit (n>n0)

big-omega -------- minimum limit

big-theat

small-o ----- (n>=no)

- O(n): 

1. for (n) ------ O(n)

2. for (n) 
            
           for (m) 
         ----------- O(n*m) ----O(n^2)

3. for (n)
for (n) 
---------- O(n)+O(n) ------ O(n)

- master theorem

T(n) = aT(n/b) + f(n) ----- first part is to divide into a parts of n/b, second part is the time for small part 

f(n):
1. <nlogba ------ O(nlogba)
2. =nlogba ------ O(nlogbalogn) = O(f(n)logn)
3. >nlogba ------ O(f(n))

bisect ---- O(logn)

sort ---- O(nlogn)

append ----- O(1)

pop --- O(1)

insert ---- O(n)

in ---- O(n)

find ---- O(n)



