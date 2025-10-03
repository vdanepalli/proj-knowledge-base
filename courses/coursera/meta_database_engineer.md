# Meta Database Engineer Professional Certificate 228h


## Introduction to Databases 27h

### Introduction to Databases

data - facts and figures
database - electronic storage and not simple files
entitites - physical or conceptual objects
relational, object-oriented, graph, document databases
nosql databases -- document, key-value, graph databases


bar chart, bubble chart, line chart, pie chart, dual axis charts, gantt charts, heat maps, scatter plots


flat files -- fixed length, separatedd
hierarchical -- one parent, multiple children -- one-to-many
network -- multiple parent child relationships -- many-to-many (owner - parent, child - member) -- SEQUEL
relational -- SQL, E.F. Codd
object-oriented -- entities/classes with attributes and behaviors
no-sql -- document, key-value, wide-column, graph
object-relational
web-enabled

CRUD Create Read Update Delete
DBMS -- SQL --> Database Instructions
- DDL Data Definition Language -- CREATE, ALTER, DROP
- DML Data Manipulation Language -- INSERT, UPDATE, DELETE
- DQL Data Query Language -- SELECT
- DCL Data Control Language -- GRANT, REVOKE
- TCL Transaction Control Language -- COMMIT, ROLLBACK

```sql
CREATE TABLE table_name (column_name1 datatype(size), column_name2 datatype(size), column_name3 datatype(size));
DROP TABLE table_name;

ALTER TABLE table_name ADD (column_name datatype(size));
ALTER TABLE table_name ADD primary key (column_name);

TRUNCATE TABLE table_name; -- Empty records

INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3);

UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;

DELETE FROM table_name WHERE condition;
```

Entity, Table, Object
Fields, Columns, Attributes
Rows, Records, Tuples, Instances
Schema, Structure

Data Types -- String, Numeric, Date and Time, Binary
- INT, TINYINT, SMALLINT, BIGINT, FLOAT, REAL
- DATE, TIME, DATETIME
- CHAR, VARCHAR
- BINARY, VARBINARY
- CLOB Character Large Object, BLOB Binary Large Object
Domains -- legal values

Primary Key (can not be null), Foreign Key, Candidate Key, Composite Key, Alternate Key, 
Integrity Constraints, Rules
- Key Constraints
- Domain Constraints
- Referential Integrity Constraints

Logical Database Structure -- represented using Entity Relationship Diagram (ERD)
Cardinality of Relationships
- One-to-one
- One-to-many
- Many-to-many

Physical Database Structure

### Numeric Data Types

Integer, Decimal
Strings
- TINYTEXT - 255 chars
- TEXT - 65000 chars
- MEDIUM TEXT - 16.7 M chars
- LONGTEXT - 4GB chars

Constraints
- NOT NULL `customerID CHAR(9) NOT NULL`
- DEFAULT `name VARCHAR(50) DEFAULT "Ash"`

```sql
CREATE DATABASE cm_devices;
USE cm_devices;
CREATE TABLE devices(deviceID INT, deviceName VARCHAR(50), price DECIMAL);
SHOW TABLES;
SHOW COLUMNS FROM devices;

CREATE TABLE customers( username CHAR(9), fullName VARCHAR(100), email VARCHAR(255));
CREATE TABLE feedback(feedbackID CHAR(8), feedbackType VARCHAR(100), comment TEXT(500));

create table address(id int not null, street varchar(255), postcode varchar(10), town varchar(30) default "Ash");

CREATE TABLE invoice(customerID VARCHAR(50), orderDate DATE, quantity INT, price DECIMAL);  
```

MySQL
- CHAR, VARCHAR, BINARY, VARBINARY, TINYBLOB, TINYTEXT, TEXT, BLOB, MEDIUMTEXT, MEDIUMBLOB, LONGTEXT, LONGBLOB, ENUM(val1, val2, ...65535 valyes) -- only one value, SET(val1, val2, ... 64 values) -- 0 or more values 
- BIT, TINYINT, BOOL, BOOLEAN, SMALLINT, MEDIUMINT, INT, INTEGER, BIGINT, FLOAT - 0 to 24, DOUBLE, DOUBLE PRECISION, DECIMAL, DEC
- DATE, DATETIME, TIMESTAMP, -- `DEFAULT` `ON UPDATE`, TIME, YEAR

MS SQL Server
- char -- n bytes | 8000 chars, varchar -- n + 2 bytes, varchar(max) -- 2GB -- non-unicode
- nchar -- 2n bytes, nvarchar, nvarchar(max) - unicode
- binary, varbinary, varbinary(max)
- bit, tinyint, smallint, int, bigint, decimal(p, s) -- 5 to 17 bytes -- p 1 to 38, s 0 to p, numeric
- smallmoney 4b,  money 8b, float(n = 24|53) -- 4b|8b, real 4b
- datetime 8b, datetime2 6-8b, smalldatetime 4b, date 3b, time 3-5b, datetimeoffset 8-10b, timestamp
- sql_variant 8000b except text/ntext/timestamp
- uniqueidentifier -- guid
- xml max 2GB
- cursor -- stores ref for cursor used
- table -- stores result-set 
- 





## Version Control 18h


## Database Structures and Management with MySQL 32h


## Advanced MySQL Topics 18h

## Programming in Python 45h


## Database Clients 40h

## Advanced Data Modeling 18h

## Database Engineer Capstone 18h

## Coding Interview Preparation 12h
