# Write your MySQL query statement below

SELECT 
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
       
FROM PERSON
LEFT JOIN ADDRESS
ON Address.personId = Person.personId;