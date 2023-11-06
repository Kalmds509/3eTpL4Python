#Enonse 1
# def inverte_mot(mot):
#     mot_invs = mot[::-1]
#     return mot_invs

# mo_kòrije = "kòrije"
# mo_invs = inverte_mot(mo_kòrije)
# print(mo_invs)

#Enonse 2
import random
import string
def jenere_kod_aleyatwa(n):
    karakters = string.ascii_letters 
    kod = ''.join(random.choice(karakters) for i  in range(n))
    return kod
kod_aleyatwa = jenere_kod_aleyatwa(10)
print(kod_aleyatwa)

#Enonse 3
def kod_aleyatwa(k):
    

