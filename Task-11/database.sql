DROP DATABASE IF EXISTS `MicroShop`;
CREATE DATABASE `MicroShop`;
USE `MicroShop`;

CREATE TABLE `Customer` (
id INT AUTO_INCREMENT NOT NULL,
`name` VARCHAR(255) NOT NULL,
PRIMARY KEY(id)
);

CREATE TABLE `Order` (
id INT AUTO_INCREMENT NOT NULL,
`date` VARCHAR(255) NOT NULL,
`total` INT NOT NULL,
PRIMARY KEY(id)
);

CREATE TABLE `OrderLine` (
id INT AUTO_INCREMENT NOT NULL,
`count` INT NOT NULL,
`total` INT NOT NULL,
PRIMARY KEY(id)
);

CREATE TABLE `Product` (
id INT AUTO_INCREMENT NOT NULL,
`name` VARCHAR(255) NOT NULL,
`price` INT NOT NULL,
PRIMARY KEY(id)
);

ALTER TABLE `Order`
ADD `customer` INT NOT NULL,
ADD FOREIGN KEY (`customer`) REFERENCES `Customer`(id);


ALTER TABLE `OrderLine`
ADD `order` INT NOT NULL,
ADD FOREIGN KEY (`order`) REFERENCES `Order`(id);


ALTER TABLE `OrderLine`
ADD `product` INT NOT NULL,
ADD FOREIGN KEY (`product`) REFERENCES `Product`(id);

CREATE TABLE Customer_Order_bind (
`Customer` INT NOT NULL,
`Order` INT NOT NULL,
FOREIGN KEY (`Customer`) REFERENCES `Customer`(id),
FOREIGN KEY (`Order`) REFERENCES `Order`(id)
);

CREATE TABLE Order_OrderLine_bind (
`Order` INT NOT NULL,
`OrderLine` INT NOT NULL,
FOREIGN KEY (`Order`) REFERENCES `Order`(id),
FOREIGN KEY (`OrderLine`) REFERENCES `OrderLine`(id)
);
