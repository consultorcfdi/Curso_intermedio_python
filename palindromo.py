def palindromo(palabra):
    palabla = palabra.replace(' ','') #con esto elimino espacios
    palabra = palabra.lower() #la convertimos a minusculas
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
      return False

def run():   #programa principal
    palabra = input("escribe una palabra ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("es Palindromo")
    else:
        print("no es palindromo")


if __name__=='__main__': #entrada del programa de Python
    run()



