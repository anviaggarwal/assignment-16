#Q.1
import pymongo
client=pymongo.MongoClient()
database=client['Students']
print('STUDENTS DATABASE CREATED')
collection=database['Student Data']
print('Students data table has been created')
#Q.2-
#Q.3
for i in range (1,11):
    print('Enter Detail Of Student {}:'.format(i))
    name=input('Name:')
    marks=int(input('Marks:'))
    collection.insert_one({'Name':name,'Marks':marks})
print('Values have been inserted')
#Q.4
data=collection.find({'Marks':{"$gt" : 80}})
for details in data:
    print('Marks greater than 80',details)
