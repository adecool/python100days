# try:
#     with open('a_file.txt') as file:
#         file.read()
# except:
#     print('file not found')
# else:
#     print('nice')
# finally:
#     print(';;;')

#FileNotFound
#
# with open('a_file.txt') as file:
#     file.read()

# #KeyError
# a_dict = {'key': 'value'}
# value = a_dict['non_existent_key']
#
# try:
#     file = open('a_file.txt')
#     a_dictionary = {"key": "value"}
#     print(a_dictionary['ssdff'])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write("something")
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist')
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError('this is an error i made up')

height = float(input('Height: '))
weight = int(input('Weight: '))
if height > 3:
    raise ValueError("human height shouldn't be greater than 3")
bmi = weight / height ** 2
print(bmi)