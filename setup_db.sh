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
  `Box #` INT NOT NULL,
  PRIMARY KEY (`Index`)
);

# Create BlackList table
CREATE TABLE BlackList (
  `Index` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(255) NOT NULL,
  `Box 1` BOOLEAN NOT NULL DEFAULT FALSE,
  `Box 2` BOOLEAN NOT NULL DEFAULT FALSE,
  `Box 3` BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (`Index`)
);

# Insert data into Residents table
INSERT INTO letter_shredder.Residents ('Name', 'Address', 'Box #')
VALUES
  ('Sahas Munamala', '1001 Main St. Apt 100', 1),
  ('Angelo Santos', '1001 Main St. Apt 101', 2),
  ('Lisa Pachikara', '1001 Main St. Apt 102', 3);

# Insert data into Blacklist table
INSERT INTO letter_shredder.BlackList ('Name', 'Box 1', 'Box 2', 'Box 3')
VALUES
  ('Amazon', FALSE, TRUE, FALSE),
  ('United Healthcare', FALSE, FALSE, TRUE),
  ('Coupons', TRUE, FALSE, FALSE),
  ('John Doe', TRUE, FALSE, FALSE),
  ('Jim Birdsong', TRUE, FALSE, FALSE);

EOF