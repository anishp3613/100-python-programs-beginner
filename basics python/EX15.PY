def exponent(base,exp):
    num=exp
    result=1
    while num>0:
        result*=base
        num-=1
    print(base," raise to ",exp,":",result)

exponent(2,5)
exponent(5,4)