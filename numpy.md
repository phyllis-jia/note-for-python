# numpy
import numpy as np

- random: 

random float number between 0 and 1(include 0) ------- np.random.random()=np.random.rand()

seed random(same seed same random) ------ np.random.seed(x)

bountary random(float) ------- random.uniform(a,b)

bountary random(integer) -------- random.randint(a,b) (b is not include)

random list -------- random.sample(range, n)

- np.arange(start, stop, step) -------- create array

- np.shape() ------ number of dimension (e.g. [1, 2, 3],[1, 3, 4])- shape[0]=2, shape[1]=3)

- xxx.dtypes == np.int64/np.object/np.float64

- arrays

1d arrays --- np.linspace(start, stop, step)

2d arrays --- image/bivariabte

3d arrays :
e.g.  u=np.linspace(x,y,z)   v=np.linspace(x,y,z)  x,y=np.meshgride(u,v)  z=x**2/25+y**2/4

- np.meshgrid() --- grib coordinate matrix

