#cleaning dara
##missing data
1. find whether there is NA
for DataFrame:

xxx.head()  xxx.tali() --- Can directly find NAN(small amount)

xxx.columns --- If result for any col has space, that col has NAN.  

xxx.shape --- number of col & row which have non-null value

xxx.info() , xxx_subset.info() --- detailed type of col (can count every column's NAN, e.g. total col:128, one specific col is 127 non-null int64, so there is 1 NA in this col )

xxx/xxx['xx'].value_counts(dropna=False) --- total number of NAN and number of non-null items for other columns (index[0]: highest frequency col)

xxx/xxx['xx'].describe() --- count, mean, std, max, min, 25%, 50%, 75%

2.deal with NA

drop na: xxx.dropna()

fill na: xxx.fillna(n)

## outlier
visulize

df.boxplot(column='y', by='x', rot=n---rotate degree) (classify the size of y based on x)(specify column and by parameters)

## duplicate

xx=xxx.drop_duplicate**s**() 

## tidy data

rules:
- columns --- separate variables
- rows --- individual observations
- observational units form tables

1. single worksheet

A. change column into rows --- melt

- xxx=pd.melt(xxx---frame, id_vars=[constant], value_vars=[change items], var_names='value_vars', value_names='id_vars')

B. turn value into columns --- pivot

- xxx=pd.pivot_table(xxx---frame, index=[primary index, secondary index...]), columns=[], values=[used data name], aggfunc=[np.sum, np.mean, n])

** pd.pivot_table(xxx, index=[field 1], values=[field 2], aggfunc=[function], fill_value=0)

=

xxx.groupby([field1])[field2].agg(function).fillna(0)**

C. slice info from data

i. slice from consecutive data

e.g. column=f14--(female, 14 years)
       
        xxx['gender']=xxx.column.str[0]

ii. slice from data with delimeter

e.g. xxx['column']=xxx['column'].str.split('delimiter')
 
        xxx['gender']=xxx.column.str.get(0/1/...)

make query to find: xxx.query('xx==['xxx']')

back to original one: xxx.reset_index()

2. multiple worksheets

A. combine different dataframes

xxx=pd.concat(**[**x,y,z..., axis=1:row wise, axis=0: column wise**]**)---- ignore_index=True, it will be no index to take

x: xxx.loc[0,:]

B. merge dataframe

xxx=pd.merge(left=dataframe, right=dataframe, left_on='column', right_on='column')

C. columns type

xxx.dtypes --- xxx's all column types, can not find specific column

xxx.xx=xxx.xx.astype('newtype') --- change column type

xxx['xx']=pd.to_numeric(xxx['xx'], errors='coerce'---na) ---- change column to numeric

pattern(yyy) making: 

i.

- *--- arbitrary number
- \d{n} --- n: n digit
- \w --- alphanumeric character
- A-Z --- any capital letter
- \$ --- $
- \. --- .
- \s --- whitespace

ii.

import re --- regular expression model

yyy=re.compile(e.g.'\d{n}-\d{n}-\d{n}) 

check if xxx is yyy: 

a. xx=yyy.match('xxx') 
print(bool(xx))

b. xx=re.match(yyy, xxx)
print(bool(xx))

check if xxx has specific type data:

xx=re.findall('/d+', 'xxx')  print(xx)--- result is list, if want specific value need slice

iii. xxx['xx']=xxx.xx/yy.apply(function)

replace x with y: xxx.xx.replace(x,y)

## test data

assert xyz.all().all() --- first all() is to test every column is true or false(series) ; second all() only return one true or false

e.g xyz is test non-null

assert pd.notnull(xxx).all().all()

xyz is test >0

assert (xxx>0).all().all()

If no result, it passes the test. Or it will have an assertionerror












