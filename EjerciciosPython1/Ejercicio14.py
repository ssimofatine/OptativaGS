### 14. Palíndromo

#Solicita al usuario una palabra e indica si es un palíndromo (se lee igual al derecho y al revés).

#---


palabra_user = input("dame palabra: ")
palabra_reves = palabra_user[::-1]

if palabra_user == palabra_reves:
    print("si es palindromo")
else:
    print("no es palindromo")