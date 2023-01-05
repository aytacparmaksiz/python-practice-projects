# The goal is adding bullet points or numerical order to the start of each line of text on the copied clipboard text.

# Bullet pointed list

import pyperclip

text = pyperclip.paste()

# TODO: Seperate lines and add stars

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)

print(text)

# If we copied the following text and run the program, 

'''
China
India
United States
Indonesia
Pakistan
Brazil
Nigeria
Bangladesh
Russia
Mexico
'''

# the result will be as follows.
'''
* China
* India
* United States
* Indonesia
* Pakistan
* Brazil
* Nigeria
* Bangladesh
* Russia
* Mexico
'''

# Ordered list

import pyperclip

text = pyperclip.paste()

# TODO: Seperate lines and add numerical order

lines = text.split('\n')
num = 1

for i in range(len(lines)):
    lines[i] = str(num) + ' ' + lines[i]
    num = num+1

text = '\n'.join(lines)
pyperclip.copy(text)

print(text)

# If we copied the following text which has population of countries and then run the program, 

''' 
China	1,452,127,674
India	1,419,655,799
United States	336,679,230
Indonesia	281,844,348
Pakistan	233,757,257
Brazil	216,641,838
Nigeria	222,182,400
Bangladesh	169,431,797
Russia	145,628,574
Mexico	132,833,767
'''
# the result will be as follows.

'''
1 China 1,452,127,674
2 India 1,419,655,799
3 United States 336,679,230
4 Indonesia	281,844,348
5 Pakistan	233,757,257
6 Brazil  216,641,838
7 Nigeria	222,182,400
8 Bangladesh	169,431,797
9 Russia	145,628,574
10 Mexico	132,833,767
'''
