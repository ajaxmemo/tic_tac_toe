starting_graphics = '''
a1 | a2 | a3
------------
b1 | b2 | b3
------------
c1 | c2 | c3
'''

is_continue = True

wining_noms = [['a1', 'a2', 'a3'],
                ['b1', 'b2', 'b3'],
                ['c1', 'c2', 'c3'],
                ['a1', 'b1', 'c1'],
                ['a2', 'b2', 'c2'],
                ['a3', 'b3', 'c3'],
                ['a1', 'b2', 'c3'],
                ['a3', 'b2', 'c1'],
               ]
user1list = []
user2list = []
print("Welcome to mimo's tic tac toe:")
print(starting_graphics)

while is_continue:
    user1_choice = input("User1's  turn : ")
    user1list.append(user1_choice)
    starting_graphics = starting_graphics.replace(user1_choice, 'o')
    print(starting_graphics)
    for nom in wining_noms:
        result1 = all(elem in user1list for elem in nom)
        if result1:
            print("user1 win")
            is_continue = False

    if not is_continue:
        break

    user2_choice = input("User2's  turn : ")
    user2list.append(user2_choice)
    starting_graphics = starting_graphics.replace(user2_choice, 'x')
    print(starting_graphics)
    for nom in wining_noms:
        result2 = all(elem in user2list for elem in nom)
        if result2:
            print("user2 win")
            is_continue = False

