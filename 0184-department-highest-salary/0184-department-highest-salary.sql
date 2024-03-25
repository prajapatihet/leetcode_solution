# Write your MySQL query statement below
select d.name as Department, e.name as Employee, e.salary as Salary from 
Department d join Employee e on e.departmentId=d.id
where (departmentId, salary) in
(select departmentId,max(salary) from Employee  group by departmentId);