#take input of a word
string = input("Enter a word: ")
#take input of a letter
char = input("Enter a letter: ")
i = 0
count = 0
#loop will to find the occurence of the letter in the word
while(i < len(string)): #string operation
  if (string[i] == char):  #condition
      count = count + 1
  i = i + 1

#display the result
print("The number of times",char,"has occureed is",count)