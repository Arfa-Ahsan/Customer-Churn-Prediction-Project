-- creating the database for customer churn prediction
create database customer_churn;

-- using that database
use customer_churn;

-- following is the sql script generated through erd plus
CREATE TABLE customers (
  customer_id VARCHAR(50) NOT NULL,
  partner ENUM('No', 'Yes') NOT NULL,
  gender ENUM('Male', 'Female') NOT NULL,
  dependents ENUM('No', 'Yes') NOT NULL,
  seniorcitizen ENUM('No', 'Yes') NOT NULL,
  PRIMARY KEY (customer_id)
);

CREATE TABLE services (
  service_id INT NOT NULL AUTO_INCREMENT,
  multiplelines ENUM('No', 'Yes', 'No phone service') NOT NULL,
  internetservice ENUM('Fiber optic', 'DSL', 'No') NOT NULL,
  onlinesecurity ENUM('No', 'Yes', 'No internet service') NOT NULL,
  onlinebackup ENUM('No', 'Yes', 'No internet service') NOT NULL,
  phoneservice ENUM('No', 'Yes') NOT NULL,
  streamingmovies ENUM('No', 'Yes', 'No internet service') NOT NULL,
  techsupport ENUM('No', 'Yes', 'No internet service') NOT NULL,
  deviceprotection ENUM('No', 'Yes', 'No internet service') NOT NULL,
  streamingtv ENUM('No', 'Yes', 'No internet service') NOT NULL,
  contract ENUM('Monthly', 'Yearly') NOT NULL,
  tenure INT NOT NULL,
  customer_id VARCHAR(50) NOT NULL,
  PRIMARY KEY (service_id),
  CONSTRAINT fk_services_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE billings (
  billing_id INT NOT NULL AUTO_INCREMENT,
  paymentmethod ENUM('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)') NOT NULL,
  paperlessbilling ENUM('No', 'Yes') NOT NULL,
  totalcharges FLOAT NOT NULL,
  monthlycharges FLOAT NOT NULL,
  customer_id VARCHAR(50) NOT NULL,
  PRIMARY KEY (billing_id),
  CONSTRAINT fk_billings_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE churn_prediction (
  prediction_id INT NOT NULL AUTO_INCREMENT,
  actual BIT NOT NULL,
  churn_prediction BIT NOT NULL,
  customer_id VARCHAR(50) NOT NULL,
  PRIMARY KEY (prediction_id),
  CONSTRAINT fk_churn_prediction_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

drop table customers;
drop table billings;
drop table services;
drop table churn_prediction;

select * from customers;
select * from services;
select * from billings;