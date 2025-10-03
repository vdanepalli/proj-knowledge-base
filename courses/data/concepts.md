# Data Concepts

## Microsoft: Azure Data Fundamentals: Core Data Concepts

Data
- Structured
- Semi-Structured (JSON, ...)
- Unstructured data

Data Stores
- File Stores
- Databases


<br/><br/>



File Stores
- Delimited text files
  - CSV Comma Separated Values
  - TSV Tab Separated Values
  - Space delimited, Fixed-Width
- JSON JavaScript Obejct Notation
- XML Extensible Markup Language
- BLOB Binary Large Object

All above are not optimized for storage or processing. 

- Avro (row-based format)
- ORC (Optimized Row Columnar format)
- Parquet (columnar data format)


<br/><br/>

Databases
- Relational -- SQL
- Non-Relational -- NoSQL
  - ket-value databases
    - Document databases -- value is JSON Object
  - Column Family databases -- tabular, but divide columns into column groups.
  - Graph databases -- entities as nodes, relations as links


<br/><br/>

Transactional Data processing
- transaction as a small, discrete, unit of work
- transactional systems are often high volume
- OLTP Online Transactional Processing. 
- Optimized for read and write operations.
- Enforces ACID semantics
  - Atomicity -- each transaction is a single unit; complete/fail
  - Consistency -- data from one valid state to other
  - Isolation -- transactions cannot interfere with one another
  - Durability -- persistent, remain committed. 
- Support live applications that process business data -- Line of Business LOB applications


Analytical Data Processing
- read-only or read-mostly systems
- OLAP Online Analytical Processing Model
- Data Lake (file-based data collection and analysis) > Data Warehouse (read optimized relational schema)> Data Lakehouses (hybrid) > OLAP/Cube (pre-aggregated) > Visualization
- Dat