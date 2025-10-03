# Pandas

## Educative: Advance Pandas Going Beyond Basics

### Introduction

- open-source, data manipulation and analysis

![Data Science and Analytics Project Life Cycle](assets/2025-05-08-17-31-56.png)


- `boto3` package is python SDK for interacting wiht AWS Services
- read web
  - read_csv
    - `read_csv(url)`
    - `read_csv(s3url, storage_options={'anon': True})`
  - read_excel
  - read_json
  - read_html
    - read_html(url) --> list of tables --> read_html(url)[0] -- table1
    - read_html(url, match="Some")
  - read_clipboard()
- read html
  - Hypertext Markup Language
  - `read_html(local_path)[0]`
  - `read_html(html_path, attrs= {'class':'wikitable'})[0]
- read xml
  - Extensible Markup Language
  - `read_xml(path)`
    ```python
    from lxml import etree

    def xml_to_df(file_path):
        with(open(file_path, 'r', encoding='utf-8')) as f:
            doc = etree.parse(f, parser = etree.XMLParser(recover=True))

        namespaces = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}

        L = []
        ws = doc.xpath('/ss:Workbook/ss:Worksheet', namespaces=namespaces)
        if len(ws) > 0:
            tables = ws[0].xpath('./ss:Table', namespaces=namespaces)
            if len(tables) > 0:
                rows = tables[0].xpath('./ss:Row', namespaces=namespaces)
                for row in rows:
                    tmp = []
                    cells = row.xpath('./ss:Cell/ss:Data', namespaces=namespaces)
                    for cell in cells:
                        tmp.append(cell.text)
                    L.append(tmp)
        df = pd.DataFrame(L[1:], columns = L[0])

        return df
    ```
- read statistical software -- SAS, SPSS, Stata
  - Data from SAS is commonly stored in SAS7BDAT binary file (.sas7bdat) or XPORT (.xpt)
    - read_sas
      ```py
      df = pd.read_sas(sas_file_path)

      with pd.read_sas(sas_file_path, chunksize=100) as rdr:
        for chunk in rdr:
            print(chunk.shape)
      ```
  - Data from SPSS -- proprietary binary format (.sav)
    - read_spss
      ```py
      df = pd.read_spss(path)

      pd.read_spss(path, usecols=['age', 'name', 'race'], convert_categoricals = False)
      ```
  - Data from Stata is stored in .dta
    - read_stata
      ```py
      pd.read_stata(path)

      pd.read_stata(path, columns=['age', 'name', 'race'])

      with pd.read_stata(path, chunk_size=100) as reader:
        for df in reader:
            print(df.shape)
      ```
- read sql databases
  - libraries
    - SQLAlchemy -- tool kit gives SQL power
    - psycopg2 -- PostgreSQL
    - PyMySQL -- MySQL
    - python-oracledb -- Oracle SQL
    - pyodbc -- Microsoft SQL Server
  - database URI Uniform Resource Identifier -- `dialect+driver://username:password@host:port/database`
  - `SELECT user()`
  - `SHOW GLOBAL VARIABLES LIKE 'PORT'`
  - ex: `mysql+pymysql://root:password@127.0.0.1:3306/adv_pandas_ch2`; `postgresql+psycopg2://username:password@host:port/database;
  ```py
  from sqlalchemy import create_engine

  uri = ...

  engine = create_engine(uri)
  
  # with is pythons context manager 
  with engine.connect() as conn, conn.begin():
    df = pd.read_sql_table('table_name', conn)

    df = pd.read_sql_table('table_name', conn, columns = ['name', 'age'], index_col = 'id')

    df = pd.read_sql_table('table_name', conn, parse_dates={'date_of_birth': '%Y-%m-%d'}, schema = 'other_schema')

  with engine.connect().execution_options(autocommit=True) as conn:
    query = conn.executre(sqlalchemy.text(sql))

  df = pd.DataFrame(query.fetchall())

  with engine.connect() as conn, conn.begin(): 
    df = pd.read_sql('query', conn) | pd.read_sql('table', conn)
    # wrapper around read_sql_table and read_sql_query
  ```
- read binary files
  - Binary files -- faster read writes, smaller storage, preserve original data structures
  - Serialization -- converting an object (data frame, dictionary) into byte sequences to be stored in binary file
  - formats -- Feather, HDF5, ORC, Parquet
  - Feather
    - .feather, `read_feather(path, columns=[])`
  - HDF5
    - .h5, `HDFStore()`, `read_hdf()`
    - made up of two object types -- datasets and groups
    ```py
    hdf = pd.HDFStore(hdf5_path)

    print("Group Hierarchy")
    for i in hdf.walk():
        print(i)

    print("group(key) names")
    print(hdf.keys())

    df1 = hdf.get('part_1_or_group_name')

    df2 = pd.read_hdf(file_path, 'part_2_group_name')
    ```
  - ORC
    - .orc, `read_orc()` -- not ideal for use
      - doesn't work for windows
      - pyarrow wheels (installed with pip)don't include ORC bindings for Linux and macOS -- so recommended to use conda
    - `pyorc` PyORC library -- read and write Apache ORC file format
    ```py
    import pyorc

    with open(path, 'rb') as orc_file:
        reader = pyorc.Reader(orc_file)
        orc_data = reader.read()
        orc_schema = reader.schema
    
    df = pd.DataFrame(data = orc_data)
    ```
  - Parquet
    - .parquet, read_parquet()
    - `pd.read_parquet(path, columns=[])`

### Combining Data

Series (one dimensional data)

- labeled array, axis labels -- index. `pd.Series(np.random.randn(5))`
- dict like behaviour. dtype
- vectorized operations   -- `s ** 2`

DataFrame (two dimensional data)
- spreadsheet or sql table
- `pd.DataFrame({"s1": pd.Series([1, 2], index=['a', 'b']) , pd.Series([1,2,3], index=['a','b','c'])})`
- each col is a Series
- `df[col]` -- col, Series
- `df.loc[label]` -- row, Series
- `df.iloc[loc]` -- row, Series
- `df[bool_vector]` `df[2:8]`

<br/><br/>


Concatenate
- row-wise axis=0 -- on top
  - `df_concat = pd.concat([dfa, dfb], axis=0, ignore_index=True)`
- column-wise axis=1 -- horizontal
  - `df_concat = pd.concat([dfa, dfb], axis=1)`
- Hierarchical indexing
  - `df_concat = pd.concat([df1, df2], keys=['2021', '2022'], names = ['Year', 'Row ID'])
  - `df_concat.index.levels` -- [['2021', '2022'], [0, 1]]`
- join='outer' or join='inner'

<br/><br/>


Merging

joins -- left outer, right outer, full outer, inner, cross
relationship types -- aka cardinalities -- 1:1, 1:M, M:N

`df = pd.merge(df1, df2, how='inner', on='id')` # left, right, outer, inner, cross

```py
pd.merge(
    left, # DataFrame as left table
    right, # DataFrame as right table
    how="inner", # Join type e.g., inner, left, right etc.
    on=None, # Keys to join DataFrames on
    left_on=None, # Columns or index levels from left table to use as keys
    right_on=None, # Columns or index levels from right table to use as keys
    left_index=False, # If True, use index from left table as join keys
    right_index=False, # If True, use index from right table as join keys
    sort=True, # Sorts output DataFrame by the join keys
    suffixes=("_x", "_y"), # Suffix string to append to names of overlapping columns
    copy=True, # If True, copies data from the passed table objects
    indicator=False, # If True, adds a column called _merge with info on data source
    validate=None, # Checks if merge is of specified type
    )

df1.merge(df2) # left join
df = pd.merge(df1, df2, how='left', on='agent_id')
df = pd.merge(df1, df2, how='cross')

df = pd.merge(df1, df2, how='outer', on='agent_id', indicator=True) # adds _merge col that has values left_only / right_only / boht

df = pd.merge(df1, df2, validate='one_to_many') # one_to_one | one_to_many | many_to_one | many_to_many
```
`join()` is used for joining DFs on index. 

```py
df.set_index('agent_id', inplace=True)

df = pd.merge(df1, df2, left_on = 'agent_id', right_index=True, how='left')

df = pd.merge(df1, df2, how='left', on=['year', 'subject'])

df.set_index(['year', 'subject'], inplace=True)
```


<br/><br/>


Compare 

```py
compare_output = df1.compare(df2) # puts marks side by side; cols -- self, other
# only displays rows where differences exist

compare_output = df1.compare(df2, keep_shape=True, keep_equal=True) # keep rows with original values even if equal
```


<br/><br/>

Combine and Update
- `combine_first()`
- `combine()`
- `update()`

```py
df_combined = df_agents_a.combine_first(df_agents_b)
# fills null values in df_agents_a with values in df_agents_b

df1.combine(other=df2, # DataFrame to combine column-wise
            func=np.minimum, # Function that is applied when combining columns (Series)
            fill_value=0, # The value to fill NaNs with prior to passing any column to the merge func
            overwrite=True # If True, columns in df1 that do not exist in df2 will be overwritten with NaN
            )


```



<br/><br/>


General

```py
df.sample(20) # random 20 rows
df.sort_values(by='col1').tail()

```

