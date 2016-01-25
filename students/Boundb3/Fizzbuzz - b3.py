# print out the numbers from 1 to n, but replace numbers divisible by 3 with "Fizz",
# numbers divisible by 5 with "Buzz". Numbers divisible by both factors should display "FizzBuzz.
# The function should be named FizzBuzz and be able to accept a natural number as argument



def FizzBuzz(n):
    for i in range(n):
        a = ""
        if (i+1)%3 == 0:
            print("Fizz", end="")
            a = "true"

        if (i+1)%5 == 0:
            print("Buzz",end="")
            a = "true"

        if a == "true":
            print("")
        else:
            print(i+1)


FizzBuzz(100)
