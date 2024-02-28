## ENCRYPTION 

def keyword_creation(message,keyword):
    i = 0
    new_keyword = [keyword]
    while len(message) >= (len(new_keyword) + len(keyword)):
        new_keyword.append(keyword[i % len(keyword)])
        i+=1
    return ''.join(new_keyword)
    
# Fonction qui faire l'addition d'index de Message et celle de Keyword et retourne letter crypte
def add_indexes(message,keyword):
    Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for k in range(len(message)):
        ecrypted_character_index = (Alphabets.index(message[k]) + Alphabets.index(keyword[k])) % len(Alphabets)
        result.append((Alphabets[ecrypted_character_index ]))
    return ''.join(result)
    
def Cryptage_Veginere(message,keyword):
    keyword_repeated = keyword_creation(message,keyword)
    return add_indexes(message,keyword_repeated)
    
# print("Message Original: ATTACKATDAWN \nKeyword : \"LEMON\"")
# print("Message crypte :",Cryptage_Veginere("ATTACKATDAWN","LEMON"))


## DECRYPTION 

def keyword_creation(message,keyword):
    i = 0
    new_keyword = [keyword]
    while len(message) >= (len(new_keyword) + len(keyword)):
        new_keyword.append(keyword[i % len(keyword)])
        i+=1
    return ''.join(new_keyword)
    
# Fonction qui faire l'addition d'index de Message et celle de Keyword et retourne letter crypte
def find_originalLetter(message,keyword):
    Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for k in range(len(message)):
        ecrypted_character_index = (Alphabets.index(message[k]) - Alphabets.index(keyword[k])) % len(Alphabets)
        result.append((Alphabets[ecrypted_character_index ]))
    return ''.join(result)
    
def Decryptage_Veginere(message,keyword):
    keyword_repeated = keyword_creation(message,keyword)
    return find_originalLetter(message,keyword_repeated)
    
# print("Message Crypte: LXFOPVEFRNHR \nKeyword : \"LEMON\"")
# print("Message Original :",Decryptage_Veginere("LXFOPVEFRNHR","LEMON"))
def Veginere():
    user_input = 100
    while user_input != 0 :
        user_input = int(input("1. Encrypter avec Veginere\n2. Decrypter avec Veginere\n0. Quitter:\n\t->  "))
        if user_input == 1: 
            msg = input("enter le message a encrypter : \t")
            motcle = input("enter un valuer pour motcle : \t")
            print("Message Encrypter:\t",Cryptage_Veginere(msg,motcle),"\n")
        elif user_input == 2 :
            msg = input("enter le message a decrypter : \t")
            motcle = input("enter un valuer pour motcle : \t")
            print("Message Original:\t",Decryptage_Veginere(msg,motcle),"\n")
        else : return 

Veginere()