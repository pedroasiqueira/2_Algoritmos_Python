def soma(n):
    if n == 0: # caso base
        return 0
    else:
        print(n)
        return n + soma(n - 1) # caso recursivo
    
print(soma(4))