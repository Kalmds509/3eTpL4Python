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

#2eme fason
# diksyone_orijinal = {"a": "12", "b": "abc", "c": "12r", "d": "90"}
# nouvo_diksyone = {kle: valye for kle, valye in diksyone_orijinal.items() if valye.isdigit()}
# print(nouvo_diksyone)


#Enonse 8
# diksyonè_orijinal = {"a": 1, "b": 2}
# lis_resulta = list(diksyonè_orijinal.items())
# print(lis_resulta)

#Enonse 9
# lis_tipl = [("a", 1), ("b", 2)]
# diksyonè_resulta = {}
# for kle,vale in lis_tipl:
#     diksyonè_resulta[kle] = vale
# print(diksyonè_resulta)

#Enonse 10
diksyone1 = {"a": 1, "b": "Kalancia", "c": [1, 2], "d": "world"}
diksyone2 = {"a": 2, "b": " St Martin", "f": [3, 4], "e": "extra"}

nouvo_diksyone = {}

for kle in set(diksyone1.keys()) | set(diksyone2.keys()):


    if isinstance(diksyone1.get(kle), int) and isinstance(diksyone2.get(kle), int):
        nouvo_diksyone[kle] = diksyone1.get(kle)+
    elif isinstance(valye1, (str, list, set)) and isinstance(valye2, (str, list, set)):
        nouvo_diksyone[kle] = valye1 + valye2

print(nouvo_diksyone)


    
    



