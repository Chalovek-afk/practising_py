me = {
    "first_name": "Alexey",
    "last_name": "Goncharov",
    "middle_name": "Pavlovich",
    "position": "Developer",
    "age": 23,
    "salary": "500$",
    True: False
}

print(me.get('first_name'))
me['position'] = 'Developer-middle'
del me[True]
print(me)