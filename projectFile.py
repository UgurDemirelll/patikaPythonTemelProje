
#Bir Listeyi düzlestiren fonksiyon
def flatter(liste,newList=[]):
    if (type(liste)==list): 
        for i in range(len(liste)):          
            flatter(liste[i],newList)
    else:
        newList.append(liste)
    return newList


#Verilen listenin içindeki elemanları ters döndüren fonksiyon
def reverser(liste):
    liste.reverse()
    print(liste)
    for i in liste:
        i.reverse()
    return liste



