-- finding out the total number of customers
select count(*) as total_customers from customers; 

-- finding out the average tenure
select avg(tenure) as avg_tenure from services; 

-- finding out the total revenue
select sum(totalcharges) as total_revenue from billings;

-- displaying customers that have a yearly contract
select gender,partner ,tenure,contract 
from customers c
inner join services s 
on c.customer_id=s.customer_id
where contract="Yearly";
 

-- Displaying customers with the equal total and monthly charges
select customer_id,totalcharges,monthlycharges from
billings where monthlycharges = totalcharges;
 
-- Displaying customers with the monthly charges greater than $70 
select customer_id,paymentmethod ,monthlycharges from 
billings where monthlycharges >70.0;

-- Advaned SQL queries

-- Calulcating the cummulative sum of total charges
select  customer_id, totalcharges,
       sum(totalcharges) over (order by billing_id) as running_total
from billings;
 
-- Displaying average of monthly charges over last 5 months
select customer_id, monthlycharges,
       avg(monthlycharges) over (order by billing_id rows between 5 preceding and current row) as  moving_average
from billings;


