#take two input from the user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print("Prime numbers between",lower,"and",upper,"are:")
#using for loop to iterate from lower to upper
for num in range(lower,upper + 1):
  #prime numbers are greater than 1
  if num > 1:
    for i in range(2,num):
     
      if (num % i) == 0:
        break
    else:
        print(num)