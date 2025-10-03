# Excel

## Coursera: Data Skills for Excel Professionals

### Fundamentals of Data Analysis In Excel

Analyzing Data

- Sorting
- Filtering
- Conditional Formatting
  - Data Bars
  - Color Scales
- Conditional Logic
  - `IF(condition, true, false)`
  - `SWITCH(expression, value1, result1, value2, result2, ....)`
  - `IFS(condition1, result1, condition2, result2, ...)`
  - `SUM(range)`
- Sumproduct  
  - `SUMPRODUCT(range1, range2)` -- SUM of products of ranges
  - `SUMPRODUCT(--(C2:C11=J14), D2:D11, E2:E11)`
- Let -- named variables  
  - `LET(variable_name, expression, expression)` => `LET(Profit, D2*E2 - D2*F2, IF(Profit > 0, Profit, "Not Profitable"))`
- Name Manager -- to the left of formula bar. can name a cell, or range, and use names in formula
- Lambda -- `LAMBDA(param1, param2, ... , expression)`
  - `LAMBDA(volume, price, cost, volume * price - volume * cost)(D2, E2, F2)`
  - `NameManagerCalcProfitability` = `LAMBDA(volume, price, cost, volume * price - volume * cost)`
    - `NameManagerCalcProfitability(D2, E2, F2)`


<br/><br/>

Transforming Data

- Text to Columns
- Removing Duplicate Values
- String Functions
  - `CONCAT(v1, v2, v3, ...)`
  - `TRIM(v1)`
  - `SUBSTITUTE(text, old_val, new_val)`
  - `LEN(val)`
  - `LEFT(val, 1)` -- fetches only 1 char from left
  - `RIGHT(val, LEN(val) - 2)` -- fetches all chars except first 2. 
  - `MID(val, startpos, num_chars)`
- Date Values

### Power Query Fundamentals

### Power Pivot Fundamentals