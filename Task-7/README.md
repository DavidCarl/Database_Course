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
    One I could think of is limiting the users to multiple ex. phonenumbers, but since there is no violation yet its hard to say.

* Second Normal Form
    Depending on if what I pointed out in first normal form is true, then its a violation of the second normal form, since it needs to be compliant with the first normal form.

## Excersise 2

### Description

Assume we did not include the customerNumber in the table. What could be a key, and do we get the same violations of the normal forms?

### Answer

Another possibility I think exist in this table could be the phone numbers, as they should be unique. Several companies cannot / should have 1 phone number, but they could have mulitple phone numbers.

// Do the normal form thingy here!

## Excersise 3

### Description

Assume the same table as in exercise 2. 

1. Write a safe update statement that change the `repPhone` column from `oldNumber` (say 12345678) to `newNumber` (say 87654321).
2. Write an update of `repEmail` which do not update properly (do not update it everywhere it should)

### Answer



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
