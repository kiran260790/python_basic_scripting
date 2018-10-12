people = {1 : {'Name':'Jhon','age':'28','Sex':'Male'},
          2 : {'Name':'wahon','age':'30','Sex':'Male'},
          3 : {'Name':'Reeta','age':'26','Sex':'Female'}}
print(people)
print('\n'*1)

#Adding the New Items into the nestead dictionary
people[4] ={}

people[4]['Name'] = 'Lama'
people[4]['Age'] = '20'
people[4]['Sex'] = 'Female'
people[4]['MatitalStaus'] = 'Unmarried'

print(people)
print("\n"*1)

#Delete Items From the Nestead Dictionary
del people[4]['MatitalStaus']
print(people)
print("\n"*1)

#Delete Items from the Dictionay
del people[4]
print(people)

#Iterating the Nested Dictionary
for p_id,p_person in people.items():
    print("\nPersons Id's =",p_id)

    for i in p_person:
        print(i + ':',p_person[i])
