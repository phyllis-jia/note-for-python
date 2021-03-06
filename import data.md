# import data
## import flat file(txt,csv)
- Flat file: table data record (no structure relationship between multiple tables) (row: fields/attributes, column: features/attributes)
                * (.txt: text file, .csv: comma separated value) *
                * (delimiter: tab, comma) *
                * (mnist digit recognation image) *
- File：Numbers -- numpy

              dataframe -- pandas 

xxx=glob.glob(...)--- download all required file, e.g. '*.csv' 

x: pd.read_csv(xxx[0])

### local flat file

1. directly

- Import: xxx=open('filename','r/w'--read/write)
- 读取result: print(xxx.read())
- Close: xxx.close()
- Check whether close: print(xxx.closed)----True/False

2. context manager

- Import: with open('filename') as xxx:
- Print first lines： print(xxx.readline())---first 

                                print(xxx.readline())---second......

3. numpy

- a. single type of data
	
   *Handwrite digit image*

  Digits = np.loadtxt('filename', delimiter=','  or '\t', skiprows=n , usecols= column used , dtype=str/float…) 
 *example code has attached*

- b. mixed type of data

e.g. str&float

data=np.genfromtxt('xxx', delimiter=',', names=True, dtype=None)

data=np.recfromcsv('xxx', , delimiter=',', names=True, dtype=None)

4. pandas(different dataframes)

xxx=pd.read.csv('xxx',  nrow=n, header=none) ---- dataframe

header: xxx.head(n) --- first n lines

- for missing data(NA/NaN):

            xxx=pd.read.csv(file, sep='/t' or ',', na_values=['Nothing'], comment='#')

            xxx.iloc[n,m]=np.nan

- check whether missing: print(xxx.isnull())  or  np.any(xxx.isnull()) == True

 if missing data: xxx.dropna(axis=0(行)/1(列), how='any'/'all')

 if filling data: xxx.fillna(value=n)

### online flat file

1. from urllib.request import urlretrieve

urlretrieve(url, 'xxx.csv') ------- save locally

df=pd.read_csv('xxx.csv', sep=';')

2. df=pd.read_csv(url, sept=';')

3. html

from urllib.request import urlopen, Request

request=Request(url)

response=urlopen(request)

html=response.read()

response.close

4. JSON -------- dictionary 

with open("a_movie.json") as json_file:

    json_data=json.load(json_file)

for k in json_data.keys():

    print(k + ': ', json_data[k])

import requests

r = requests.get(url)

json_data=r.json()

5. API

import tweepy

access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"

access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"

consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"

consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token,access_token_secret)

## import excel
### local excel file

1. pickle (serialize data)

with open(xxx, r/b- read/binary) as xxx:

xx=pickle.load(xxx)

2.pandas (Excel)

xxx=pd.ExcelFile('xxx')

sheet names: xxx.sheet_name**s** or xxx.keys()

sheet head: xxx['sheet name'].head()

event: 
- single sheet: xxx.phase(n---index/'x')
- multiple sheets: xxx.phase(n---sheet number(first:0), names=['x'], usecols=[], skiprows=[])

### online excel file

xxx=pd.read_excel(url, sheetname=None)

## import SAS/State
pandas

1. SAS

from sas7bdat import SAS7bdat

with SAS7BDAT('') as xxx:

   xx=xxx.to_data_frame() ------- change into dataframe

head: x_sas.head()

2. state

xxx=pd.read_state('')

## import HDF5 (large quantities of numerical data)

numpy

import h5py

xxx=h5py.**F**ile('', 'r/w')

event: xx=xxx[''][''].value

## import MATLAB

scipy.io

import scipy.io

xxx=scipy.io.loadmat('') --- (type: dict)

xxx[''] --- (type: numpy array)

## import SQL

sqlalchemy & pandas

From sqlalchemy import create_engine

Xxx=create_engine('sqlite:///filename') 
 
Table_names= xxx.table.names()

1. Xxx=create_engine('sqlite:///filename')                 ------ import file by create engine

  Con=Xxx.connect()                                                      ------ connection 

  Xx=con.execute('SELECT */column name1 FROM table name1 INNER JOIN table name2 on  table name1. column name2=table name2.column name 2 WHERE condition ORDER BY column name')     ------ select table

  X=pd.DataFrame(Xx.fetchall())                                 ------ dataframe
  
  Con.close()                                                                   ------ close

2. Context manager ( no need to close)

 Xxx=create_engine('sqlite:///filename')   
             
 with Xxx.connect() as con:      
        
        xx=con.execute('SELECT */column name1 FROM table name1 INNER JOIN table name2 on  table name1. column name2=table name2.column name 2 WHERE condition ORDER BY column name' )     
        
        X=pd.DataFrame(xx.fetchmany(size=n)          ------- many here is different from all in 1 (many need to choose amount of size, all is all)
        
        X.columns = xx.keys()                                ------- make column

3. Xxx=create_engine('sqlite:///filename')

 xx=pd.read_sql_query('SELECT */column name1 FROM table name1 INNER JOIN table name2 on  table name1. column name2=table name2.column name 2 WHERE condition ORDER BY column name', Xxx)

E.g 'SELECT */column name1 FROM table name1 INNER JOIN table name2 on  table name1. column name2=table name2.column name 2 WHERE condition ORDER BY column name'  
    
      'SELECT title, name FROM order INNER JOIN artist on order.id=artist.id WHERE sales >= 6 ORDER BY birthdate'








