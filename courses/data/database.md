# Database

## Educative: Database Design Fundamentals for Software Engineers

### Fundamentals

- File-based System
- cons
  - Data redundancy -- many places to update/delete
  - Data inconsistency -- multiple copies 
  - Difficult data access
  - Security problems
  - Difficult concurrent access -- file gets locked once opened


<br/><br/>

- Database: Shared collection of related data (facts); 
  - represents mini-world or Universe of Discourse (UoD)
  - logically coherent collection of data with some inherent meaning
- DBMS: Database Management System -- collection of programs
  - Defining
  - Constructing
  - Manipulating
  - Sharing
- Database System -- DBMS Software + Database
- Table  -- collection of related data in rows and cols
  - each row is one instance of the object -- record
  - cols are set of facts -- attribute
- Characteristics of database
  - Self describing nature of database system -- data + meta-data describing data and relationships
  - Insulation between program and data -- program-data independence
  - Support for multiple views of data -- view as subset of database
  - Sharing data and multiuser system -- concurrency control strategies
- Benefits of Database
  - Control of data redundancy
  - Data sharing
  - Enforcement of Integrity Constraints -- restriction/rule
  - Restriction of unauthorized access -- user accounts, access privileges
  - Backup and recovery facilities -- protect data from loss


### Data Modeling 

- Data  Models help achieve data abstraction -- hide irrelevant details
- A collection of concepts or notations for describing data, data relationships, data semantics, data constraints
- types
  - high-level conceptual data models
    - Entity-Relationship model
      - Entities (real world object)
      - Attributes (properties)
      - Relationships (associations among entities)
  - Record-based logical data model
    - Hierarchical -- tree like structure; only one paretn for each child
    - Network -- graph structure; can have more than one parents
    - Relational -- relations or tables
  - Physical data model -- each table, cols, specifications etc; represents how data is stored in computer memory
- Database Schema -- blueprint of database
  - Schema Evolution -- changes to schema
- Database Instance -- database state; snapshot


<br/><br/>

- Three-Schema Architecture -- separate user applications from physical database
  - External Level -- External Schema -- View 1, View 2, ... say for each role or user type
  - Conceptual Level -- Conceptual Schema -- database structure for community of users -- record-baased logical data model
  - Internal Level -- Internal Schema -- how data is stored physically -- physical data model
- Data Independence -- change database schema at one level without changing schema at next highest level
  - Logical data independence -- changes at Conceptual Level should not affect External Level
  - Physical data independence -- changes to Internal Schema doesn't affect Conceptual/External Schemas


<br/><br/>


- Classification of DBMS
  - Based on Data Model
    - Relational -- Oracle and RDB - Oracle, MS SQL Server and Access, DB2 and Informic Dynamic Server - IBM, MySQL, ... -- table oriented
    - Object Oriented Data Models (OODBMS) -- O2, ObjectStore, Jasmine, ...
  - Based on Number of Users
    - Single-user
    - Multi-user
  - Based on database distribution
    - Centralized systems -- DBMS and Database are central
    - Distributed systems
    - Homogenous Distributed Systems -- use same DBMS software
    - Heterogenous Distributed Systems -- can use different DBMS software
      - same Machine Readable Catalogging MARC -- bibliographic information -- appendix


### Entity Relationship Model

- ER Models aka ER Schemas are represented by ER Diagrams
- Entity -- real world object (physical or conceptual)
- Entity type -- collection or set of entities that have same attributes -- rectangle box
- Entity set -- collection of all entities of an entity type


<br/><br/>

- Attributes -- oval 
  - Simple attributes -- atomic (single) value -- cannot divide further
  - Composite attributes -- hierarchy of attributes -- can divide into further attributes
  - Multivalued attributes -- can have a set of values for entity -- double oval
  - Derived attributes -- calculated from stored attributes (physically stored) -- dashed oval
- Keys -- key or uniqueness -- primary key -- name underlined inside oval
  - Composite Key -- set of attributes uniquely identifying entity -- composite attribute designated as key attribute


<br/><br/>

- Relationships -- associations between entities
- Relationship type -- relation between entities -- diamond shaped box
- Relationship set -- set of similar associations at a point of time
- Degrees of relationship types -- number of participating entity types
  - Unary (Recursive) -- same entity type -- employee and supervisor
  - Binary -- links two entity types -- employee works_on project
    - Binary relationship type constraints
      - Mapping Cardinality -- maximum participating entities -- 1:1, 1:N, N:N
      - Participation -- specified if existence of an entity depends on it being related to another entity via relationship type
        - Total Participation aka mandatory participation -- each entity has a relationship instance -- double line between entity set and relationship set
        - Partial Participation aka optional participation -- single line
  - Ternary -- Supplier supplies parts to projects
- Relationship types can have their own attributes but we don't want that if we don't need that
  - 1:1 -- can move attribute to either table
  - 1:N -- move attribut to the table with N
  - M:N -- forced to move attribute to the relationship instead of tables
- Weak Entity types -- do not have key attributes of their own -- double rectangle
  - has a partial key -- oval with name underlined with dashed line -- uniquely identifies entity for a specific owner entity
  - always has a total participation with its identifying relationship (double diamond box)
- Strong entity types -- have key attribute -- single rectangle
- Identifying or Owner Entity type -- used to link to Weak Entity type using Identifying relationship


### Relational Data Model

- introduced by C F Codd in 1970
- database as a collection of relations
- relation is a table of values
- tuple is a record in a relation
- relation schema -- relation name with its attributes
- degree of the relation -- number of attributes
- cardinality -- number of tuples
- relation  instance -- set of tuples
- domain -- original set of atomic models used to model data -- set of acceptable values


<br/><br/>

- table properties
  - each row is unique
  - values are atomic
  - column values are of the same type -- same domain
  - sequence of columns/rows is insignificant
  - each col has a unique name
- keys
  - super key -- set of attributes that can uniquely identify record
  - candidate key -- minimal set of fields required to uniquely identify -- can be null or empty or a comnbination of cols
  - primary key -- a choosen candidate key
  - composite key -- two or more attributes uniquely identifying record but individually don't 
  - alternate key -- candidate key other than primary key
  - foreign key -- refers to the primary key of other table to establish a link
- constraints -- rules forcing DBMSs to check data satisfies semantics
  - relational integrity constraints -- must be present for a valid relation -- an arc from foreign key to primary key with arrow pointing to primary key
    - domain constraints
    - entity integrity  -- every relation needs to have primary key and cannot be NULL
    - referential integrity -- all values taken by foreign key must be available in primary key or be null
      - can not add foreign key without having corresponding primary key in referenced table
      - can not delete primary key from referenced table if its being referenced as foreign key in referencing relation
  - key constraints


<br/><br/>

- Relatonal Database Schema S is a set of relation Schemas (R1, R2, ...) and a set of integrity constraints IC
- Relational Database State DB of S is a set of relation states (r1, r2, ...) each ri is a state of Ri
- Operations
  - Insert -- can violate domain/key/entity integrity/referential integrity constraints, 
  - Delete -- can only violate referential integrity -- restrict (reject), cascade (delete corresponding)
  - Update -- updating primary key col(s) is same as deleting and inserting, and above come into play


### Functional Dependencies

- A functional dependency is a relationship between two attributes, typically PK and other non-key attributes. 
- X (determinant) -> Y (dependent) if X uniquely identifies Y (instance - person, can have same name but person itself is different)
- Rules
  - Armstrong’s axioms