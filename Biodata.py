print('Welcome to the interactive biodata program!','\n')

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
height = float(input('Please enter your height in meters: '))
favnum = int(input('Please enter your favorite number: '))

print('\nThank you for providing your information! Here is your biodata:','\n')
print('Name:', name, type(name))
print('Age:', age, type(age))
print('Height:', height, 'm', type(height))
print('Favorite Number:', favnum, type(favnum))

print('Your birth year is:', 2026 - age)
print('\nThank you for using the interactive biodata program! Have a great day!')