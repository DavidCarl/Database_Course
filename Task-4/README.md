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
Book keeper hasn't been given ```DELETE``` privilige either since we dont want our information to be deleted. They have also been given ```SELECT```, ```INSERT```, ```UPDATE``` on the payment and order tables. But there has only been given ```SELECT``` on customer table as there is no need for them to change in customer detail.

#### Human Ressources
Human Ressources has been given ```SELECT```, ```INSERT```, ```UPDATE``` on the employee table aswell as the offices table. This is because they would need to update employment status etc.

#### Sales
Sales will be given ```SELECT```, ```INSERT```, ```UPDATE``` rights on the customer table, order and order details table, and ```SELECT``` on product table. That way around they can edit customer information if needed and orders, they can get a overview on product information aswell.

#### IT
IT would be given all access depending on their status in the IT department because they need it for maintance in the long run and for whatever support there is requested from the other departments.

## Assignment 2
First we need to get into the Docker container running MySQL.
```docker exec -it mysql /bin/bash```

Then we need to log into our MySQL server.
```mysql -u {username} -p```
For us its looking like this ```mysql -u root -p``` then it request a password, write yours there.

Once here you can run these 2 mysql commands
```
Execute SET GLOBAL log_output = 'TABLE';
Execute SET GLOBAL general_log = 'ON';
```

You should use this command to see your log

```select event_time, user_host, CONVERT(argument USING utf8 ) as sqlcommand from mysql.general_log```

A screenshot from out log looks like [this](https://i.imgur.com/z3xejQm.png)!

## Assignment 3

To make a dump you can run the following command
```docker exec -i mysql mysqldump -u root -p classicmodels > dump.sql```

We have used the mysqldump tool that is build into MySQL to perform our dump. The reason we choose this is because it is build into MySQL so everyone should have the ability to use the same command as we did.

To load a dump you can run the following command, it is required you have a database called classicmodels!
```docker exec -i mysql classicmodels < dump.sql```