def countdown(n):
  numberPar = 0
  # print(range(n+1))
  for number in range(n+1):
    if number % 2 == 0 and number != 0:
      numberPar += 1

  return numberPar

def countdown_recursivo(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + countdown_recursivo(n-1)
    else:
       return countdown_recursivo(n-1)