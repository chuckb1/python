
# def countDown(num):
#     my_list = []
#     for x in range(num,-1,-1):
#         my_list.append(x)
#     print(my_list)
# countDown(5)

# def print_and_return(x,y):
#     print(x)
#     return(y)
# print_and_return(1,2)


# def first_plus_length(my_list):
#     return my_list[0] + len(my_list)
# print(first_plus_length([1,2,3,4,5]))   


# def greater_than_second(my_list):
#     new_list = []       
#     for x in range(0,len(my_list)):
#         if len(my_list) < 2:
#             return False
#         if my_list[x] > my_list[1]:
#             new_list.append(my_list[x])
#     print(len(new_list))
#     return new_list
        
# listofstuff = [5,2,3,2,1,4]
# print(greater_than_second())

def length_and_value(length, value):
    new_list = []
    for x in range(0,length):
        new_list.append(value)
    return new_list

print(length_and_value(6,2))

