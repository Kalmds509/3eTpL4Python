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
# diksyonè = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
# for kle in diksyonè.keys():
#     print(kle)
   
#Enonse 4 
# diksyonè = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
# for vale in diksyonè.values():
#     print(vale)

#Enonse 5
# diksyonè_orijinal = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
# diksyonè_kopi = {}
# for kle, valè in diksyonè_orijinal.items():
#     diksyonè_kopi[kle] = valè
# print(diksyonè_kopi)

#2eme fason
# diksyonè_orijinal = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
# diksyonè_kopi = diksyonè_orijinal.copy()
# print(diksyonè_kopi)

#Enonse 6
# diksyonè = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}
# for kle, valè in diksyonè.items():
#     if isinstance(valè,str):  # Verifye si valè a se yon chenn
#         diksyonè[kle] = "_" + valè + "_"
# print(diksyonè)

#Enonse 7
# diksyone={"a": "12", "b": "abc", "c": "12r", "d":"90"}
# diksyone2={}
# for kle,vale in diksyone.items():
#     if vale.isdigit():
#         diksyone2[kle]=vale
# print(diksyone2)

#Enonse 8
diksyonè_orijinal = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
diksyonè_kopi = list(diksyonè_orijinal.copy())
print(diksyonè_kopi)


