#find if a number entered from user is divisible
#by 3 or by 5. If a number is divisible by 3, print fizz
#if a number is divisible by 5, print buzz
# if both, print fizzbuzz
input = int(input("Please enter a number: "))
if input%3==0 and input%5==0:
    print("fizzbuzz")
    exit()
if input%3==0:
    print("fizz")
if input%5==0:
    print("buzz")
