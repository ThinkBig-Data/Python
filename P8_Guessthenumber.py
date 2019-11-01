import random

takeguess = 0
print("hello, what's your name ? ")
inputname = input()

number= random.randint(1, 30)
print("well, "+ inputname + " let me think of a number b&w 1 to 30.")
print("   ")
print("remember you will get only 4 chances")
print("   ")
while takeguess < 4:
    print("take a guess !")
    guess=int(input( "from 1 to 30\n"))

    takeguess=takeguess+1

    if guess< number:
        print("your guess is too low !")

    if guess>number:
        print("your guess is too high !")
    if guess== number:
        break

if guess==number:
    takeguess=str(takeguess)
    print('Good job, ' + inputname + '! You guessed my number in ' + takeguess + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)