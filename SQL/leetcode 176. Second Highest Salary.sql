-- https://leetcode.com/problems/second-highest-salary/

-- ifnull 과 order by 사용해도되고 window function을 이용해서 row_number 이용해도 될듯함.

SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
