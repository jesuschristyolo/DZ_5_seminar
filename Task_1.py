 #Напишите программу, которая на вход принимает два числа A и B
#, и возводит число А в целую степень B с помощью рекурсии.


def degree (a: int, b : int) -> int:
  if b == 0:
     return 1
  return a * degree(a,b - 1)
  #return a**b


print(degree(3,5))