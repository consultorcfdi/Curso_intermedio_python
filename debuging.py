def divisor(num):
    divisors = []
    for i in range (1, num + 1):
        if num % 1 ==1:
           divisors.append(i)
    return divisors 


def run():
    num = int(input("ingresa un numero"))
    print(divisor(num))
    print("termino mi programa")

if __name__=='__main__':
    run()