# victoria calvin 082318

arr_list = ['victoria', 'calvin', 'henry']

# for firstname in arr_list:
#     print(firstname)

# arr_size = len(arr_list)

# my_range = range(0, arr_size)

# for i in my_range:
#     print(i)

# print(my_range)

# something_list = ['something', 'goes', 'in', 'here']

# for word in something_list:
#     print(word)

# something_size = len(something_list)

# something_range = range(0, something_size)

# for i in something_range:
#     print(i)
#     print(something_list[i])
    
doggy = {
    "name": "max",
    "breed": "cockapoo",
    "age": 5
}

kitten = {
    "name": "bronson",
    "breed": "mustache cat",
    "age": 2
}

pets = [doggy, kitten]

# for pet in pets:
#     print(pet["name"])

# for pet in pets:
#     print(pet["breed"])
#     print(pet["age"])
    
def give_info(pet_dict):
    return "{} {} {}".format(pet_dict['name'],pet_dict['breed'],pet_dict['age'])

# string_pets = map(give_info, pets)

# print(string_pets)

def capitalize_name(name):
    return name.capitalize()

capitalized_names = map(capitalize_name, arr_list)

print(capitalized_names)