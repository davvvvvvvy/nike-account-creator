import string
import sys, os

f = open('accounts.txt', 'r+')
accs = []
for line in f.readlines():
    for value in line.split(':'):
        accs.append( value )
f.close()
n=1
i=0
final = [accs[i * n:(i + 1) * n] for i in range((len(accs) + n - 1) // n )]
for j in range(0, len(final)):
    accs_email = final[0:len(final):2]
    accs_pass = final[1:len(final):2]
ks = len(final)//2
for k in range(0, len(final)//2):
    print(accs_pass[k])
