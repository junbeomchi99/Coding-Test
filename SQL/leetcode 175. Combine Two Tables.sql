-- https://leetcode.com/problems/combine-two-tables/
-- simple join problem
select firstName, lastName, city, state
from Person a
left outer join Address b
on a.personID = b.personID
