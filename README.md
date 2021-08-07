### HR_API 

Requirements           | Endpoint                | Code implementation
---------------------- | ----------------------- | ------------
Read all (sorting, pagination, filtering provided as parameters) | v1/profiles/?ordering=salary&page=4 and other params | class ProfilesList()
Read one               | v1/profiles/<int:pk>/   | class ProfileSingle()
Update one             | v1/profiles/<int:pk>/   | class ProfileSingle()
Delete one             | v1/profiles/<int:pk>/   | class ProfileSingle()
Average age per industry | v1/age/<str:industry> | class AverageAge()
Average salaries per industry| v1/salary/industry/<str:industry> | class AverageSalary()
Average salaries per years of experience | v1/salary/experience/<int:experience> | class AverageSalaryPerExperience()
Interesting statistics | v1/salary/prediction    | 
Basic validation       |  -                      | Included in framework
Database               |  -                      | Postgres
API docs at v1/docs