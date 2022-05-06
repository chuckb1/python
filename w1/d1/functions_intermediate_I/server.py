x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# def change_last_name(x):
#     students[0] ['last_name'] = x

# change_last_name('Bryant')
# print(students[0])

# def change_value_of_x(n):
#     x[1][0] = n

# change_value_of_x(15)
# print(x[1][0])

# def change_sports_dir(p):
#     sports_directory['soccer'] = p

# change_sports_dir('Andre')
# print(sports_directory['soccer'])

# def change_value_of_z(n):
#     z[0]['y'] = n

# change_value_of_z(30)
# print(z[0]['y'])

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(some_list):
    
#     for i in range(0,len(some_list)):
#         print(f"first_name - {some_list[i] ['first_name']} last_name - {some_list[i] ['last_name']}")
# iterateDictionary(students)

# def iterateDictionary2(key_name, some_list):
    
#     for i in range(0,len(some_list)):
#         print(f"{some_list[i] [key_name]}")
# iterateDictionary('first_name', students)

# def iterateDictionary2(key_name, some_list):
    
#     for i in range(0,len(some_list)):
#         print(f"{some_list[i] [key_name]}")
# iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for val in some_dict.values():
        # print(len(some_dict.values()))
        print(len(val))
        # print(val)
        for item in val:
            print(item)
            
printInfo(dojo)