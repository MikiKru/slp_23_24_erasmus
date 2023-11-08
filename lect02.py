# STRING

name = 'script language programming'
print(name)
print(name[2])

name = 'python programming'
print(name)
print(len(name))
print(name[0:6])  # first - included, last - excluded
print(name[:6:2])  # first - included, last - excluded

# LIST
list2d = [[1, 2, 3], [4, 5, 'six'], [7, 8, 9]]
print(list2d[1][2][2])

# DICTIONARY
simple_translator = {
    'cat': ['kot', 'gato', 'kedi'],
    'ok': ['spoko', 'perfecto', 'tamam']
}

print("PL", simple_translator['cat'][0])
print("ES", simple_translator['cat'][1])
print("TR", simple_translator['cat'][2])

# SET VS FROZENSET

s1 = {1, 2, 3}  # mutable
s2 = {2, 3, 4, 5}  # mutable
s3 = frozenset([1, 2, 3])  # immutble

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)


