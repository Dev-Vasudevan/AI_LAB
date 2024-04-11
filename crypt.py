def crypt (a,b,c):
    letters = list(set(a+b+c))
    numbers = set([ i for i in range (9)])
    dic = {}
    permute(letters, numbers, dic, a, b, c)

def permute ( letters , numbers ,dic,a,b,c ):
    if len(letters)==0:
        return

    for number in numbers:
        dic[letters[0]] = number
        numcopy = numbers.copy()
        numcopy=numcopy.difference({number})
        permute(letters[1:],numcopy,dic,a,b,c)
        if len(letters )==1:
            if compute(a,b,c,dic):
                print(dic)
                print("DONE")
                exit(1)

def compute (a,b,c , dic ):
    num1=0
    num2=0
    num3=0
    for i in a:
        num1*=10
        num1+= dic[i]

    for i in b:
        num2*=10
        num2+= dic[i]

    for i in c:
        num3*=10
        num3+= dic[i]

    if (num1+num2==num3):
        print(f"{num1},{num2},{num3}")
        print(a,b,c)
        return True
    return False



crypt('SEND','MORE','MONEY')

