# List Comprehension Structures #

list1 = ["blue", "black", "purple", "yellow", "red"]

comprehension0 = ["Bilge" for i in list1]
# ['Bilge', 'Bilge', 'Bilge', 'Bilge', 'Bilge']

comprehension1 = [colour for colour in list1]
# ['blue', 'black', 'purple', 'yellow', 'red']

comprehension2 = [i for i in list1 if "u" in i]
# ['blue', 'purple']

###########################################

list2 = [1000, 1200, 1400, 1600, 1800, 2000]

comprehension3 = [i / 4 if i <= 1600 else i * 2 for i in list2]
# [250.0, 300.0, 350.0, 400.0, 3600, 4000]

comprehension4 = [(i, j) for i, j in enumerate(list1)]
# [(0, 'blue'), (1, 'black'), (2, 'purple'), (3, 'yellow'), (4, 'red')]

comprehension5 = [(i, j) for i, j in enumerate(list1) if i % 2 == 0]
# [(0, 'blue'), (2, 'purple'), (4, 'red')]

###########################################


comprehensions = [i ** 3 for i in range(1, 10)]
print("Cubic numbers are:", comprehensions)
# Cubic numbers are: [1, 8, 27, 64, 125, 216, 343, 512, 729]

colours = ["Blue", "Black", "Brown", "Green", "White", "Pink", "Turquoise", "Lilac"]

bad_colours = ["Pink", "Turquoise", "Lilac"]

comprehension6 = [color.lower() if color in bad_colours else color.upper() for color in colours]
# ['BLUE', 'BLACK', 'BROWN', 'GREEN', 'WHITE', 'pink', 'turquoise', 'lilac']

comprehension7 = ["Yes" if i not in bad_colours else "No" for i in colours]
# ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No']

#####################################################
# Dictionary_Comprehensions #

list3 = [99, 100, 101, 102, 103, 104, 105, 106]

dict_comprehension = {i: i - 99 for i in list3}
# {99: 0, 100: 1, 101: 2, 102: 3, 103: 4, 104: 5, 105: 6, 106: 7}

dict1 = {"Blue": 5, "Green": 4, "Black": 3, "Purple": 2, "Orange": 1, "Pink": 0}

dict_comp1 = {i.upper(): j * 2 for (i, j) in dict1.items()}
# {'BLUE': 10, 'GREEN': 8, 'BLACK': 6, 'PURPLE': 4, 'ORANGE': 2, 'PINK': 0}

dict_comp2 = {i.upper(): j for (i, j) in dict1.items() if j % 2 == 0}
# {'GREEN': 4, 'PURPLE': 2, 'PINK': 0}

#################################################

numbers = range(8)

dict_comp3 = {i: i * 2 for i in numbers if i % 2 == 0}
# {0: 0, 2: 4, 4: 8, 6: 12}

# Set Comprehensions #


list_set = [1, 1, 2, 2, 2, 5, 6, 7, 7, 7, 7]

comprehension_Set ={i for i in list_set}
# {1, 2, 5, 6, 7}
