# [Data Warehousing](../../courses.md)

- [Data Warehousing](#data-warehousing)
  - [LinkedIn: Introduction to Data Warehouses](#linkedin-introduction-to-data-warehouses)


## LinkedIn: Introduction to Data Warehouses

- Data Warehouse
  - large
  - built on top of a database
- Customer buys product -> Database -- ETL Process --> Data Warehouse
- OLTP Online Transaction Processing Database
  - Say Sales, Operations, Customer Service -- each a separate database
- OLAP Online Analytical Processing
  - Data Warehouse
- OLTP data copied to OLAP
- Data Lake
  - centralized repository storing structured and unstructured data
  - Store data in raw format
- Structured data
  - well defined schema
- Data Warehouse
  - Stores structured data
  - Better for cleaned, transformed, and organized data
- Data Mart
  - Smaller, more focused version of data warehouse
  - designed to provide specific, targeted information to a specific group
- ETL Extract Transform Load
  - Tools
    - SSIS
    - Informatica
- Traditional Solutions
  - Teradata
    - RDBMS
    - Scalability and High Performance
    - Commonly used in Telecommunications and Finance
  - IBM DB2
    - RDBMS
    - Robustness and Reliability
    - Common - Retail and Healthcare
  - Oracle Database
    - RDBMS 
    - Flexibility and Scalability
    - Finance and Manufacturing industries
  - Microsoft SQL Server
    - RDBMS
    - Small and Medium-Size businesses
  - MySQL
    - Open-source RDBMS
    - Small and Medium-Size ecommerce and web development
  - PostgresSQL
  - SQLite


<br/><br/>

- Dimensional Modeling: Technique used to organize and structure data in data warehouse; creates a model that is optimized for querying and analysis
- Facts
  - Measurable and Aggregable
  - Quantitative values
  - Usually additive
- Dimensions
  - Context for facts/measurements
  - Categorizing facts or information
  - Ex
    - Date table
- Key dimensional modeling alternatives
  - Data vault modeling
    - complex and rapidly changing environments
    - separates data into hubs (core business entities) links(relationships between entities) and satellites (descriptive data)
  - Wide tables (denormalized structures)
    - combines fact and dimension data into a single, wide table to minimize joins and optimize read performance
    - performance-oriented analytics -- higher storage costs and maintenance challenges
  - Data lakehouse architecture
    - integrates benefits of data lakes and data warehouses
    - organizes data into a layered approach with raw, cleansed, and aggregated data
    - supports schema evolution
    - ideal for modern analytics and mixed workloads
  - Entity-relationship modeling
    - creating detailed relationships between data entities, offering comprehensive mapping of complex relationships
    - commonly used in operational databases but can be adapted for analytical purposes if detailed relationships are needed
  - Hybrid modeling
    - combines aspects of different modeling techniques to cater to unique business requirements
- Star Schema
  - Multidimensional data model 
  - Has a central fact table
  - Has multiple dimension tables
  - Benefits
    - better data organization
    - query performance
    - data aggregation
  - faster performance
- Snowflake Schema
  - Multidimensional data model
  - More normalized and complex
  - Benefits
    - efficient at storing and retrieving data
    - querying
    - can handle large data
    - eliminate data redundancy
    - consistency
  - slower performance


<br/><br/>

- Install SQL Server
- Install SSMS SQL Server Management Studio
- Create a Database and tables inside it. Use Database Diagrams to create relationships using GUI
- Cloud Data Warehouse
  - hosted on cloud servers
  - Scale up or down
  - Cost-effective (storage and processing power)
  - Accessible
  - Has built-in tools
  - Security and Privacy concerns
  - Slower data transfer
- On-premises
  - physical DW
  - Installed and maintained on company's servers
  - Fast & Reliable
  - Expensive and Time consuming
  - Limited in scalability


<br/><br/>

- Amazon Redshift
  - fully-managed petabyte-scale DW Service
  - Integrates with other AWS Services
    - Amazon S3
    - Amazon EMR
- Microsoft Azure Synapse Analytics
  - fully-managed petabyte-scale DW Service
  - structured and unstructured data
  - Integrates with Services
    - Azure Data Factory
    - Azure Databricks
- Google BigQuery
  - fully-managed serverless DW Service
  - Integrates with
    - Cloud Storage
    - Looker Studio
- Snowflake
  - cloud-native data waerhouse
  - structured and unstructured
  - scalable (separates compute and storage)