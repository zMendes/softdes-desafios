## Adding students

To add students, first you need to create a CSV file named "users.csv" with their names and roles:

```caio,student```


Then, you will need to create the database:

`$ sqlite3 quiz.db < quiz.sql`

Adding users to the database:

`$ python3 adduser.py`


## Adding new quizzes

To add quizzes, you will have to manually insert the quiz in the database with a SQL script.

Example of a SQL query adding a quiz:  
```Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values (1, '2018-08-01','2022-12-31 23:59:59','Exemplo de problema','[[1],[2],[3]]','[0, 0, 0]','["a","b","c"]');```
