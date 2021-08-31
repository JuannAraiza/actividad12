def main():
    #escribe tu código abajo de esta línea

    c = 0      #contador
    s = 0      #acumulador

    while (s < 1000):
        n = int(input('Dame un número: '))
        s = s + n 
        c = c + 1 
    
    print(f'Suma es igual a: {s}')
    print(f'Cantidad de números es igual a: {c}')

    


if __name__=='__main__':
    main()
