# Task-7

### Made by David Carl & Tjalfe Møller
### www.dcarl.me

### Overall information

Consider this select statement from classic models:

```select customerNumber,
       customerName,
       concat(contactFirstName,' ', contactLastName) as contactName,
       customers.phone as contactPhone,
       customers.city as custCity,
       customers.postalCode as custZip,
       customers.country as custCountry,
       concat(firstName,' ',lastName) as repName,
       employees.email as repEmail,
       offices.phone as repPhone,
       offices.postalCode as repZip,
       offices.city as repCity,
       concat(offices.addressLine1, '\n', offices.addressLine2) as repAddress,
       offices.country as repCountry
from employees 
inner join customers on employees.employeeNumber = customers.salesRepEmployeeNumber
inner join offices on employees.officeCode = offices.officeCode
```
Assume it to be materialized into a table CustomerOverview.

## Excersise 1

### Description

Mention which violation there are to:

* First normal form (if any)
* Second normal form (if any)
* Third normal form (if any)

### Answer

* First Normal Form
    When running this query there is no primary key that is represented, so that violates one of the requirements.

* Second Normal Form
    Since the First Normal Form is violated this is also considered violated as its dependent on it!

* Third Normal Form
    Due to the relation between our Zip and City fields in our customer and rep part of the table. This violate the Third Normal Form aswell as the Second Normal Form not being complaint.

## Excersise 2

### Description

Assume we did not include the customerNumber in the table. What could be a key, and do we get the same violations of the normal forms?

### Answer

In this case we could treat the customerName as a sort of username, and make it our primary key, but for it to be a primary key we would need it to force unique values. As the customers first and last name is stored elsewhere.  
Another possibility I think exist in this table could be the phone numbers, as they should be unique. Several companies cannot / should have 1 phone number, but they could have mulitple phone numbers.

But the customerName would probably be the safest, as could have multiple instances and not forced to have diferent phonenumbers.


* First Normal Form
    As the table would have a primary key represented and all columns have a single domain, there is no violations.

* Second Normal Form
    No violations.

* Third Normal Form
    Due to the relation between our Zip and City fields in our customer and rep part of the table. This violate the Third Normal Form.


## Excersise 3

### Description

Assume the same table as in exercise 2. 

1. Write a safe update statement that change the `repPhone` column from `oldNumber` (say 12345678) to `newNumber` (say 87654321).
2. Write an update of `repEmail` which do not update properly (do not update it everywhere it should)

### Answer

This snippet is our safe SQL update method

```
UPDATE <Table_Name>
SET repPhone = '87654321'
WHERE repPhone = '+1 212 555 3000'
```

This is out unsafe snippet

```
UPDATE <Table_Name>
SET repEmail = '87654321@rep.com'
WHERE customerNumber = '103'
```

The reason why our safe method works is because it goes in, and find all occurences of that phone number and replace it by the new one. Where our unsafe only find a specific customer and update the phone number there.


## Excersise 4

### Description

In this exercise we will assume we have materialized this query into a table `tblEx4Sydney`.

```sql
with my_cust as
   (select customerNumber,
       customerName,
       customers.country as custCountry,
       offices.city      as repCity
    from employees
       inner join customers on employees.employeeNumber = customers.salesRepEmployeeNumber
       inner join offices on employees.officeCode = offices.officeCode)
select *
from my_cust
where repCity = 'Sydney'
```

Assume we have an index on customerName, and assume a fan-out in the B+ tree of 4. 

**Draw** a representation of of the B+ tree with index and leaf nodes, as well as the actual table data. The drawing must be a combination of Figure 1.1 and 1.2 from [Anatomy of an SQL index](https://use-the-index-luke.com/sql/anatomy).

### Answer
