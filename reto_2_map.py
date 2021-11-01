#convertir una lista de numeros a otra con sus cuadrados  usando ciclo for
# y usando despues  list comprehesion
# 

def run():
    # list = [1,2,3,4,5]

    #esto es con ciclo for
    # for i in list:
    #     lista =[i**2]
    #     print(lista)

    #esto fue con list comphemsion
    
    # list =[i**2 for i in list]
    # print(list)


    #esto es con map
    my_list = [1,2,3,4,5]
    squares = list(map(lambda x: x**2, my_list))
    print (squares)


if __name__=='__main__':
    run()