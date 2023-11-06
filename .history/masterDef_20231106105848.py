import random
import string
#Enonse 1
def inverte_mot(mot):
    mot_invs = mot[::-1]
    return mot_invs

mo_kòrije = "kòrije"
mo_invs = inverte_mot(mo_kòrije)
print(mo_invs)

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
# def kod_alfa_nimerik(n):
#     nim="123456789"
#     alfa_nim=string.ascii_letters+nim
#     kod=''.join(
#         random.sample(alfa_nim,n))
#     return kod
# rezilta=kod_alfa_nimerik(5)
# print(rezilta)

#Enonse 5
# def jenere_slug(chenn):
#     slug = ''
#     for karaktè in chenn:
       
#         if karaktè.isalnum() or karaktè == '-':
#             slug += karaktè
#         else:
#             slug +="-"
#     slug = slug.strip("-")
#     slug = slug.lower()
#     return slug
# chenn = "C'est un slug."
# slug = jenere_slug(chenn)
# print(slug)

#Enonse 6
# def mo_vigil(mot):
#     result=','.join(mot)
#     return result
# test=mo_vigil("ale")
# print(test)

#Enonse 7
# def kriptaj(mo):
#     let=string.ascii_uppercase
#     result=""
#     for i in range(len(let)):
#         if(let[i] in mo):
#             result+=str(i)+"-"
#     result= result[:-1]
#     return result
# t=kriptaj("ALO")  
# print(t)

#Enonse 8
# def dekriptaj(kriptaj):
#     let=string.ascii_uppercase
#     tab=kriptaj.split('-')
#     result=""
#     for i in tab:
#         result+=let[int(i)]
#     return result
# print(dekriptaj("0-11-14"))
 
#Enonse 9
# def pemitasyon(premye,dezyem):
#     t=[]
#     temp=premye
#     premye=dezyem
#     dezyem=temp
#     t.append(premye)
#     t.append(dezyem)
#     t=tuple(t)
#     return t
# print(pemitasyon("1","2"))

#Enonse 10
# def inisyal(non):
#     non=non.replace("-"," ")
#     t_non=non.split(" ")
#     result=""
#     for i in t_non:
#         result+=i[0]
#     return result
# print(inisyal("jean-marc baptiste"))


