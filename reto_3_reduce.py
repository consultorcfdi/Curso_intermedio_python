from functools import reduce


def run():
    #vamos a reducir una lista  multiplicando todos sus elementos internamente 
    #primero con el ciclo for
    my_list = [2,2,2,2,2]
    result=1
    
    #aqui es con cicl for
    # for i in my_list:
    #     result=result*i
    
    # print (result)

    #aqui es con  list comphernsion

    #como result no es una lista no aplica
#     print (result)
#con reduce queda asi
    all_multiplied = reduce(lambda a, b:a*b,my_list)
    print(all_multiplied)




if __name__=='__main__':
    run()
