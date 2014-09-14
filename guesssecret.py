__author__ = 'Ali'
print"Please think of a number between 0 and 100!"
high = 100
low = 0
ans = int((high+low)/2)
numguess=1
while numguess<50:
    print"Is your secret number "+str(ans)+" ?"
    g = raw_input("Enter 'h' if it is too high. Enter 'l' if it is too low. Enter 'c' to indicate I guessed correctly:")
    if g == "h":
        high = ans
    elif g == "l":
        low = ans
    elif g == "c":
        break
    else:
        print"Sorry, I did not understand your input."
    numguess += 1
    ans = int((high+low)/2)

print"Game over. Your secret number was: "+str(ans)
print"Number of guesses was: "+str(numguess)


