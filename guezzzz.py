#a = secret number
#b = number of guesses  allowed
#c = number of guesses made
#d = guess made by the user

a = 5
b = 3
c = 0

while c < b :
    c = c + 1
    d = int(input("Enter a guess: "))
    if d == a :
        print("Yayy you got it correct")
        break
    if c == 1 :
        print("Hint : 1-10")
    if c == 2 :
        print("You have to get it this time!")
else :
    print("You ran out of tries. Better luck next time!")
    print("The secret number was 5")
