# plt

import matplotlib.pyplot as plt

- plt.plot(x, y, color='r/b...')

- plt.axes([left, bottom, width, height]) ---- parameter: 0-1(figure dimension) ---- use to identify different figures, or there may be many curves in one figure

- plt.subplot(nrows, ncols, index, kwargs) = fig.add_subplot(nrows ncols index)---- create subplot: divide screen into grib which has nrows, ncols, index is the position in grib

- plt.tight_layout() --- examine axis label, scale label and title, partly adjust parameters, in order to let plot full in plot range

- plt.xlabel('name'), plt.ylabel('name')

- plt.xlim((range)), plt.ylim((range)) = plt.axis((xrange, yrange)) 

axis('off')= truns off axis lines, labels ; axis('equal')= equal scaling on x, y axes ; axis('square')= forces square plot --- adjust axis range to chage plot into square one; axis('tight')= sets xlim(), ylim() to show all data

- plt.savefig('name.png') --- save

- plt.scatter(x, y, marker='./....', label=, color=, s(size)=)

- plt.legend(loc=) ---- comment 

code: 0='best', 1='upperright', 2='upperleft', 3='lowerleft', 4= 'lowerright', 5='right', 6='centerleft', 7='centerright', 8='lowercenter', 9='uppercenter'

- plt.annotate() ---- arrow and comment of it 

s: text of label; xy: coordinates to annotate; xytest: coordinates of label, arrowprops={facecolor=''} --- controls drawing of arrow

- argmax(): for certain axis, it will return to max index of this axis

- plt.style.use('ggplot'...)

- plt.pcolor(z/x, y, z, cmap='blue''grey''autumn'/none) ---- pseudocolor image(react value with color, when value is higher, color is deeper)

- plt.colorbar()

contour image: 
- plt.contour(x,y,z,n): contours as lines
- plt.contourf():: filled areae between contours

- plt.hist(x, y, bins=(v*u rectangle), range=((x1, x2, y1, y2))) ---- rectangle bin

- plt.hexbin(x, y, extent=(x1, x2, y1, y2), gridsize=(number of x axis hexbin, number of y axis hexbin)

image
- color image: RGB(red-green-blue)
- channel value: 0-1(floating print number), 0-255(8 bit integer)
- read: xxx=plt.imread('name')
- display: plt.imshow(xxx, extent=(x1,x2, y1, y2), cmap=, aspect=n)

- plt.clf(): clean up

- plt.show()



