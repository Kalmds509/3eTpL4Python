#Enonse 1
limit=12
divizib_2=[]
for i in range(limit+1):
    if(i%2==0):
        divizib_2.append(i)
print(divizib_2)

#Enonse 2
# list_antye = [1, 2, 3, 4, 5, 6, 7, 8]
# list_chenn = []
# for elem in list_antye:
#     list_chenn.append(str(elem))
# print(list_chenn)

#Enonse 3
# list_chenn_miniskil=["ayiti","canada","france"]
# list_chenn_majiskil=[]
# for i in list_chenn_miniskil:
#     list_chenn_majiskil.append(i.upper())
# print(list_chenn_majiskil)

#Enonse 4
# liste = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15]
# nouvo_lis = []
# for i in range(len(liste)):
#     if i % 3 == 0:
#         nouvo_lis.append(liste[i])
# print(nouvo_lis)

#Enonse 5
# liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# nouvo_lis = []
# for i in range(0, len(liste), 3):
#     groupe = (liste[i], liste[i + 1],liste[i+2])
#     nouvo_lis.append(groupe)
# print(nouvo_lis)

#Enonse 6
# lis_avek_doublon = [1, 2, 2, 3, 4, 4, 5, 6, 6,7,8,7,9,12,3,6]
# retire_doublon = set(lis_avek_doublon)
# lis_sans_doublon = list(retire_doublon)
# print(lis_sans_doublon)

#Enonse 7
# lis1 = [1, 2, 3, 4, 5]
# lis2 = [3, 4, 5, 6, 7]
# lis_komen=[i for i in lis2 if i in lis1]
# print(lis_komen)

#Enonse 8
# lis1 = [1, 2, 3, 4, 5]
# lis2 = [3, 4, 5, 6, 7]
# lis_distenk=[i for i in lis1 if i not in lis2 ]+[k for k in lis2 if k not in lis1]
# print(lis_distenk)

#Enonse 9
# diksyone={'kle1':1,'kle2':2,'kle3':3,'kle4':4}
# list_kle=list(diksyone.keys())
# lis_vale=list(diksyone.values())
# print(list_kle)
# print(lis_vale)

#Enonse 10
# lis1 = [1, 2, 3, 4, 5]
# lis2 = [3, 4, 5, 6, 7]
# lis3 = [5, 6, 7, 8, 9]
# nouvo_lis = [i for i in lis1 + lis2 + lis3]
# san_doublon = set(nouvo_lis)
# lis_final = list(san_doublon)
# print(lis_final)





