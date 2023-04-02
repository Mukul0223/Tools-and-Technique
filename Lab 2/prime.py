num = int(input("Enter a number:"))
a=2
while num > a :
  if num%a==0 & a!=num:
    print('not prime')
    break
  a+= 1
else:
  print('prime')


