#Enonse 1
# diksyone={'kle1':1,'kle2':2,'kle3':3,'kle4':4}
# for i in diksyone:
#     print(diksyone[i])

#Enonse 2
# vale=input("ekri yon vale")
# if(len(vale)>=2 and vale[0]=="{" and vale[-1]=="}"):
#     print("Nou verifye li gen akolad devan ak deye:  ")
# else:
#     print("Pa gen akjolad evan ak deye")

#2eme fason
# import re
# valè = input("Tape yon valè : ")
# patwon = re.compile(r'^\{.*\}$')

# if patwon.match(valè):
#     print("Valè a gen akolad devan ak dèyè.")
# else:
#     print("Valè a pa gen akolad devan ak dèyè.")

#Enonse 3
diksyonè = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}

for kle in diksyonè.values():
    print(kle)

