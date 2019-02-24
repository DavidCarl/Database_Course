# Task-2

### Made by David Carl & Tjalfe Møller
### www.dcarl.me

## Assignment 1

### Description

Inventory - which is used to maintain the two tables ```products``` and ```productlines```.
Book keeper - which make sure that all orders are payed.
Human resources - which takes care of employees and their offices
Sales - who creates the orders for the customers
IT - who maintains this database

### Answer

#### Inventory Manager
Inventory managers will be given ```SELECT```, ```INSERT```, ```UPDATE``` privileges, since they need to be able to update manufactors and products itself. They also need to be able to insert new manufactors and products, and last see whats already is in there.

There have not been given the privilige to ```DELETE``` since stuff should newer be deleted!

#### Book Keeper
Book keeper hasnt been given ```DELETE``` privilige either since we dont want our information to be deleted. They have also been given ```SELECT```, ```INSERT```, ```UPDATE``` on the payment and order tables. But there has only been given ```SELECT``` on customer table as there is no need for them to change in customer detail.

#### Human Ressources
Hum Ressources has been given ```SELECT```, ```INSERT```, ```UPDATE``` on the employee table aswell as the offices table. This is because they would need to update employment status etc.

#### Sales
Sales will be given ```SELECT```, ```INSERT```, ```UPDATE``` rights on the customer info, and ```SELECT``` on product information, and order info. That way around they can edit customer information if needed and they can get a overview on product information aswell as orders to help the customers if needed.

#### IT
IT would be given all access depending on their status in the IT department because they need it for maintance in the long run and for whatever support there is requested from the other departments.

## Assignment 2

## Assignment 3