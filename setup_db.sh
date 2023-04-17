# Log in to MySQL as root
sudo mysql -u root << EOF

# Create user and grant privileges
CREATE USER 'smunamala'@'localhost' IDENTIFIED BY 'raspberry';
GRANT ALL PRIVILEGES ON *.* TO 'smunamala'@'localhost';

# Create Residents table
CREATE TABLE letter_shredder.Residents (
  Index INT NOT NULL AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  BoxNo INT NOT NULL,
  PRIMARY KEY (Index),
  UNIQUE (Index)
);

# Create BlackList table
CREATE TABLE letter_shredder.BlackList (
  Index INT NOT NULL AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Box1 BOOLEAN NOT NULL,
  Box2 BOOLEAN NOT NULL,
  Box3 BOOLEAN NOT NULL,
  PRIMARY KEY (Index),
  UNIQUE (Index)
);

# Insert data into Residents table
INSERT INTO letter_shredder.Residents (Name, Address, BoxNo)
VALUES
  ('Sahas Munamala', '1001 Main St. Apt 100', 1),
  ('Angelo Santos', '1001 Main St. Apt 101', 2),
  ('Lisa Pachikara', '1001 Main St. Apt 102', 3);

# Insert data into Blacklist table
INSERT INTO letter_shredder.Blacklist (Name, Box1, Box2, Box3)
VALUES
  ('Amazon', FALSE, TRUE, FALSE),
  ('United Healthcare', FALSE, FALSE, TRUE),
  ('Coupons', TRUE, FALSE, FALSE),
  ('John Doe', TRUE, FALSE, FALSE),
  ('Jim Birdsong', TRUE, FALSE, FALSE);

EOF