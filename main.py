def main():
    
    
    user_input = int(input("choisir une methode:\n1. Cesar\n2. RSA\n3. Veginere\n4. Affine\n\t-> "))
    # Teste de Methode de Cesar
    if(user_input == 1) : from Cesar import Cesar
    elif(user_input == 2) : from Rsa import Rsa
    elif(user_input == 3) : from Veginere import Veginere
    else : return

main()