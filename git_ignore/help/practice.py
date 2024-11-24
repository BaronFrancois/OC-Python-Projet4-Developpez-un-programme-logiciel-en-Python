# list1 = [1, 2]
# list2 = [3, 4]
# print(list1 + list2)
# clubs = [['London Chess Club', 'Paris Chess Club'], ['Indian Chess Club', 'Japan Chess CLub']]
# flat_list = []
# for club in clubs:
#     print(club)
#     flat_list = flat_list + club
#     # flat_list.append(club)

# print(flat_list)

# def add(a, b):
#     return (a + b)

# add = lambda a, b: (a + b)
players = [
            {
                "first_name": "Johan",
                "last_name": "Doe",
                "date_of_birth": "1990-05-14",
                "national_chess_id": "EN12345"
            },
            {
                "first_name": "Jane",
                "last_name": "Smith",
                "date_of_birth": "1988-11-20",
                "national_chess_id": "EN67890"
            }
        ]

def find_longest(my_list, max_rule):
    longest_str = max(my_list, key = max_rule)
    return longest_str

# def lambda_copy(item):
#     return len(item['first_name'])


longest_first_name = find_longest(players, lambda item: len(item['first_name'])) #item with longest name
longest_first_name = len(longest_first_name['first_name'])
print(longest_first_name)
