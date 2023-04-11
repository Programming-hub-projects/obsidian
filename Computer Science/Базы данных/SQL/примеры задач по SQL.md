Для проведения тестирования, в Oracle 11g была развернута схема, содержащая следующие таблицы:  
  
![](https://habrastorage.org/r/w1560/storage2/fa2/06e/d3d/fa206ed3d94ff2c063afbe2a03c7df81.png)  
  
Требовалось составить SQL-запросы, для решения следующих пяти заданий:  

**Задание 1**
Вывести список сотрудников, получающих заработную плату большую чем у непосредственного руководителя
```sql
select a.* 
from employee a, employee b 
where b.id = a.chief_id and a.salary > b.salary
```

**Задание 2**
Вывести список сотрудников, получающих максимальную заработную плату в своем отделе  

**Вариант ответа**

```sql
select a.*
from   employee a
where  a.salary = ( select max(salary) 
					from employee b
                    where  b.department_id = a.department_id )
```

**Задание 3**

Вывести список ID отделов, количество сотрудников в которых не превышает 3 человек  

**Вариант ответа**
```sql
select department_id
from   employee
group  by department_id
having count(*) <= 3
```

**Задание 4**
Вывести список сотрудников, не имеющих назначенного руководителя, работающего в том-же отделе  
  
**Вариант ответа**

```sql
select a.*
from   employee a
left   join employee b on (b.id = a.chief_id and b.department_id = a.department_id)
where  b.id is null
```

**Задание 5**
Найти список ID отделов с максимальной суммарной зарплатой сотрудников  
  
**Вариант ответа**
```sql
with sum_salary as
  ( select department_id, sum(salary) salary
    from   employee
    group  by department_id )
select department_id
from   sum_salary a       
where  a.salary = ( select max(salary) from sum_salary ) 
```