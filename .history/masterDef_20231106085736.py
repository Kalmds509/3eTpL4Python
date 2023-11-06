import random
import string
#Enonse 1
# def inverte_mot(mot):
#     mot_invs = mot[::-1]
#     return mot_invs

# mo_kòrije = "kòrije"
# mo_invs = inverte_mot(mo_kòrije)
# print(mo_invs)

#Enonse 2

# def jenere_kod_aleyatwa(n):
#     karakte = string.ascii_letters 
#     kod = ''.join(random.choice(karakte) for i  in range(n))
#     return kod
# kod_aleyatwa = jenere_kod_aleyatwa(10)
# print(kod_aleyatwa)

#Enonse 3
# def kod_aleyatwa(k):
#     let=string.ascii_letters
#     let_tire=random.sample(let,k)
#     code=''.join(let_tire)
#     return code
# kod=kod_aleyatwa(5)
# print(kod)

#Enonse 4
def kod_alfa_nimerik(n):
    nim="123456789"
    alfa_nim=string.ascii_letters+nim
    kod=''.join(random.sample(alfa_nim,n))
rezilta=kod_alfa_nimerik(5)
print(rezilta)

    

