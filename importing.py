#import file practice

with open('pi_million_digits.txt') as f:
    lines = f.readlines()

pstring = ''
for line in lines:
    pstring += line.strip()
#print(pstring)
if input('What is your birthday as number?') in pstring:
    print('yes')
else:
    print('sorry')
    
