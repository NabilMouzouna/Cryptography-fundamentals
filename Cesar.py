def Cesar_crypter(message,k):
    if message == "" : return "le message est vide"
    Alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for index in range(len(message)) :
        for j in range(len(Alphabet)):
            if message[index] == Alphabet[j]: result.append(Alphabet[(j + k) % len(Alphabet)])
    return "".join(result)


####################################################################################################################

def Cesar_decrypter(message,k):
    if message == "" : return "le message est vide"
    Alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for index in range(len(message)) :
        for j in range(len(Alphabet)):
            if message[index] == Alphabet[j]: result.append(Alphabet[(j - k) % len(Alphabet)])
    return "".join(result)

def Cesar():
    user_input = 100
    while user_input != 0 :
        user_input = int(input("1. Encrypter avec Cesar\n2. Decrypter avec Cesar\n0. Quitter:\n\t->  "))
        if user_input == 1: 
            msg = input("enter le message a encrypter : \t")
            decalage = int(input("enter un valuer pour decalage : \t"))
            print("Message Encrypter:\t",Cesar_crypter(msg,decalage),"\n")
        elif user_input == 2 :
            msg = input("enter le message a decrypter : \t")
            decalage = int(input("enter un valuer pour decalage : \t"))
            print("Message Original:\t",Cesar_decrypter(msg,decalage),"\n")
        else : return 

Cesar()