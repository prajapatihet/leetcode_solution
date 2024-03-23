# select if(count(salary)=0,null,salary) as SecondHighestSalary from (select salary,dense_rank() over (order by salary desc) as dnk from Employee) dnkemp where dnkemp.dnk=2;

with hs as(
select max(salary) as mx from Employee
)
select max(salary) as SecondHighestSalary from Employee where salary<(select hs.mx from hs);