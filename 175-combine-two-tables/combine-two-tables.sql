# Write your MySQL query statement below
select firstname, lastname, city , state
from Person left join address
on person.personID= address.personID;

