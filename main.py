import random

options = ['piedra', 'papel', 'tijera']

user_option = input('¿Piedra, papel o tijera? ')

user_option = user_option.lower()
cpu_option = random.choice(options)
match = (user_option, cpu_option)

if user_option == cpu_option:
    print (f'Empata contra {cpu_option}')
elif match == ('piedra','tijera'):
    print (f'Le gana a {cpu_option}')
elif match == ('papel','piedra'):
    print (f'Le gana a {cpu_option}')
elif match == ('tijera','papel'):
    print (f'Le gana a {cpu_option}')
else:
    print (f'Pierde contra {cpu_option}')
