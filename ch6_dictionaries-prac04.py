
# there are several ways to loop through a dictionary, such as a FOR loop
user_1 = {
    'username': 'BdB',
    'first': 'Brittany',
    'last': 'Del Bryant'
}
# using two variables to store the key and value pairs; and also the keyword '.items()'
for key, value in user_1.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

