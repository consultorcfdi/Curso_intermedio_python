def run():
    # sqrts = []

    # for i in range (1,101):
        
    #     if i%3 !=0:
    #         sqrts.append(i**2)
        
    #     print(sqrts)

    # sqrts =[i**2 for i in range (1,101) if i%3 !=0]
    # numeros = [i for i in range (1,100000) if i%4 ==0 and  i%6 ==0 and  i%9==0]
    numeros = [i for i in range (1,100000) if i%36 == 0]


    print(numeros)

if __name__=="__main__":
    run()