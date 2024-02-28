import random
def gcd(a,b):
    while b != 0: a,b = b, a % b
    return a
def est_premier(n):
    for i in range(2 , int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def inv_mod(a,m):
    m0,x0,x1 = m,0,1
    while a > 1:
        q= a // m
        m,a = a % m,m
        x0,x1 = x1 - q * x0,x0
    return x1 + m0 if x1 < 0 else x1

def cle():
    p = random.randint(50,1000)
    q = random.randint(50,1000)
    while not est_premier(p) : 
        p = random.randint(50,1000)
    while not est_premier(q) : 
        q = random.randint(50,1000)
    n = p*q
    m = (p-1)*(q-1)
    while True :
        e = random.randint(10,m)
        if gcd(e,m) == 1: break
    d = inv_mod(e,m)
    return ((e,n),(d,n))
           
def RSA():
   user_input = 100
   public,privee = cle()
   while user_input != 0 :
       user_input = int(input("1. Encrypter avec RSA\n2. Decrypter avec RSA:\n0. Quitter:\n\t->  "))
       if(user_input == 1 ) :message = input("Entrer votre message:\t")
       elif user_input ==  0 : return
       else : 
        messageChar =input("Entrer votre message encrypter sous cette forme des numbers separer par vergule:\t")
        message = []
        messageChar = messageChar.split(",")
        for char in messageChar : message.append(int(char))

       if user_input == 1 :
            e,n = public
            message_encrypter = [pow(ord(char),e,n) for char in message]
            print("\nmessage encrypter: ",message_encrypter,"\n")
       else :
            d,n = privee
            original_message = [chr(pow(char,d,n)) for char in message]
            print ("\nmessage Original: ","".join(original_message),"\n")

print(RSA())
