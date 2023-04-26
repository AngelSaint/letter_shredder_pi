# Log in to MySQL as root
sudo mysql -u root << EOF

# Create the letter_shredder database
CREATE DATABASE letter_shredder;

USE letter_shredder

# Create Residents table
CREATE TABLE Residents (
  `Index` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(255) NOT NULL,
  `Address` VARCHAR(255) NOT NULL,
  `Apartment` INT UNSIGNED NOT NULL,
  `Box#` INT NOT NULL,
  PRIMARY KEY (`Index`)
);

# Create BlackList table
CREATE TABLE BlackList (
  `Index` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(255) NOT NULL,
  `Box1` BOOLEAN NOT NULL DEFAULT FALSE,
  `Box2` BOOLEAN NOT NULL DEFAULT FALSE,
  `Box3` BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (`Index`)
);

# Insert data into Residents table
INSERT INTO letter_shredder.Residents ("Name", "Address", "Apartment", "Box#")
VALUES
  ("Angelo Santos", "123 Main Street", 100, 1),
  ("Sahas Munamala", "123 Main Street", 101, 2),
  ("Lisa Pachikara", "123 Main Street", 102, 3);

# Insert data into Blacklist table
  INSERT INTO letter_shredder.BlackList
  VALUES
    (1, "Verizon", TRUE, TRUE, FALSE),
    (2, "Amazon", FALSE, TRUE, FALSE),
    (3, "United Healthcare", FALSE, FALSE, FALSE);

EOF